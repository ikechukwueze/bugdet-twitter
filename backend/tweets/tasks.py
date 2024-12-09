import string
from django.db.models import QuerySet
from accounts.models import Account
from timeline.models import TimeLine
from followers.models import Follower
from tweets.models import Tweet
from notifications.models import NotificationType
from trends.trend_analysis import analyse_tweet_trends
from celery import shared_task
from utils.helpers import create_notification


def clean_username(username_token: str):
    return username_token.rstrip(string.punctuation)


def detect_username_mention(content):
    username_tokens = [token[1:] for token in content.split() if token.startswith("@")]
    mentions = [clean_username(token) for token in username_tokens]
    return mentions


def push_tweet_to_user_timeline(tweet: Tweet):
    timeline_tweet = TimeLine.objects.create(tweet=tweet)
    timeline_tweet.viewers.add(tweet.author)


def push_tweet_to_followers(tweet: Tweet):
    account = tweet.author
    try:
        timeline_tweet = TimeLine.objects.get(tweet=tweet)
    except TimeLine.DoesNotExist:
        pass
    else:
        account_followers = Follower.objects.filter(account=account)
        followers = [obj.follower for obj in account_followers]
        timeline_tweet.viewers.add(*followers)


def create_mention_notification(tweet: Tweet):
    sender = tweet.author
    mentions = detect_username_mention(tweet.content)
    for username in mentions:
        try:
            recipient = Account.objects.get(username=username)
        except Account.DoesNotExist:
            continue
        else:
            create_notification(
                sender=sender,
                recipient=recipient,
                recipient_tweet=None,
                sender_tweet=tweet,
                notification_type=NotificationType.MENTION,
            )


def tweet_processing_pipeline(tweet: Tweet):
    push_tweet_to_user_timeline(tweet)
    push_tweet_to_followers(tweet)
    create_mention_notification(tweet)
    analyse_tweet_trends(tweet)


@shared_task
def create_like_notification(sender: Account, recipient: Account, liked_tweet: Tweet):
    notification = create_notification(
        sender=sender,
        recipient=recipient,
        recipient_tweet=liked_tweet,
        sender_tweet=None,
        notification_type=NotificationType.LIKE,
    )
    return notification


@shared_task
def create_dislike_notification(
    sender: Account, recipient: Account, disliked_tweet: Tweet
):
    notification = create_notification(
        sender=sender,
        recipient=recipient,
        recipient_tweet=disliked_tweet,
        sender_tweet=None,
        notification_type=NotificationType.DISLIKE,
    )
    return notification


def create_retweet_notification(
    sender: Account, recipient: Account, reposted_tweet: Tweet
):
    notification = create_notification(
        sender=sender,
        recipient=recipient,
        recipient_tweet=reposted_tweet,
        sender_tweet=None,
        notification_type=NotificationType.RETWEET,
    )
    return notification


def create_quote_notification(
    sender: Account, recipient: Account, quoted_tweet: Tweet, quote: Tweet
):
    notification = create_notification(
        sender=sender,
        recipient=recipient,
        recipient_tweet=quoted_tweet,
        sender_tweet=quote,
        notification_type=NotificationType.QUOTE,
    )
    return notification


def create_reply_notification(
    sender: Account, recipient: Account, original_tweet: Tweet, reply_tweet: Tweet
):
    notification = create_notification(
        sender=sender,
        recipient=recipient,
        sender_tweet=reply_tweet,
        recipient_tweet=original_tweet,
        notification_type=NotificationType.REPLY,
    )
    return notification


def mark_notification_as_read(notifications_qs: QuerySet):
    pass


@shared_task
def process_tweet(tweet_id: int):
    tweet = Tweet.objects.get(id=tweet_id)
    tweet_processing_pipeline(tweet)


@shared_task
def process_reply_tweet(tweet_id: int):
    tweet = Tweet.objects.get(id=tweet_id)
    tweet_processing_pipeline(tweet)
    create_reply_notification(
        sender=tweet.author,
        recipient=tweet.referenced_tweet.author,
        reply_tweet=tweet,
        original_tweet=tweet.referenced_tweet,
    )


@shared_task
def process_quote_tweet(tweet_id: int):
    tweet = Tweet.objects.get(id=tweet_id)
    tweet_processing_pipeline(tweet)
    create_quote_notification(
        sender=tweet.author,
        recipient=tweet.referenced_tweet.author,
        quoted_tweet=tweet.referenced_tweet,
        quote=tweet,
    )


@shared_task
def process_retweet(tweet_id: int, reposted_tweet_id: int):
    tweet = Tweet.objects.get(id=tweet_id)
    reposted_tweet = Tweet.objects.get(id=reposted_tweet_id)
    push_tweet_to_user_timeline(tweet)
    push_tweet_to_followers(tweet)
    create_retweet_notification(
        sender=tweet.author,
        recipient=reposted_tweet.author,
        reposted_tweet=reposted_tweet,
    )
