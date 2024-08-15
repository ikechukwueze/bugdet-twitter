from datetime import datetime
from typing import List
from django.utils.timezone import make_aware
from django.utils import timezone
from django.db.models import QuerySet, F
from accounts.models import Account
from timeline.models import TimeLine
from followers.models import Follower
from tweets.models import Tweet
from notifications.models import Notification, NotificationType


def reformat_tweet_timestamp(timestamp_str: str):
    input_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    output_format = "%H:%M · %d %b %y"

    timestamp = datetime.strptime(timestamp_str, input_format)
    timestamp = make_aware(timestamp)
    time_difference = timezone.now() - timestamp
    seconds_passed = time_difference.total_seconds()

    one_minute = 60
    one_hour = one_minute * 60
    one_day = one_hour * 24
    day_limit = one_day * 2

    if seconds_passed < one_minute:
        return f"{int(seconds_passed)}s"

    elif one_minute < seconds_passed < one_hour:
        return f"{int(seconds_passed // one_minute)}m"

    elif one_hour < seconds_passed < one_day:
        return f"{int(seconds_passed // one_hour)}h"

    elif one_day < seconds_passed < day_limit:
        return f"{int(seconds_passed // one_day)}d"

    return datetime.strftime(timestamp, output_format)


def clean_username(username_token: str):
    punctuations = [".", ",", "/", "\\", "!", "?"]

    while username_token[-1] in punctuations:
        username_token = username_token[:-1]

    return username_token


def detect_username_mention(content):
    username_tokens = [token[1:] for token in content.split() if token.startswith("@")]
    mentions = [clean_username(token) for token in username_tokens]
    return mentions


def push_tweet_to_timeline(tweet: Tweet):
    timeline_tweet = TimeLine.objects.create(tweet=tweet)
    timeline_tweet.viewers.add(tweet.author)


def push_tweet_to_followers(account: Account, tweet: Tweet):
    try:
        timeline_tweet = TimeLine.objects.get(tweet=tweet)
    except TimeLine.DoesNotExist:
        pass
    else:
        account_followers = Follower.objects.filter(account=account)
        followers = [obj.follower for obj in account_followers]
        timeline_tweet.viewers.add(*followers)


def create_notification(
    sender: Account,
    recipient: Account,
    sender_tweet: Tweet,
    recipient_tweet: Tweet,
    notification_type,
):
    if sender != recipient:
        notification = Notification.objects.create(
            sender=sender,
            recipient=recipient,
            sender_tweet=sender_tweet,
            recipient_tweet=recipient_tweet,
            notification_type=notification_type,
        )
        return notification


def create_follow_notification(sender: Account, recipient: Account):
    notification = create_notification(
        sender=sender,
        recipient=recipient,
        recipient_tweet=None,
        sender_tweet=None,
        notification_type=NotificationType.FOLLOW,
    )
    return notification


def create_mention_notification(sender: Account, tweet: Tweet):
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


def create_like_notification(sender: Account, recipient: Account, liked_tweet: Tweet):
    notification = create_notification(
        sender=sender,
        recipient=recipient,
        recipient_tweet=liked_tweet,
        sender_tweet=None,
        notification_type=NotificationType.LIKE,
    )
    return notification


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


def create_retweet_notification(sender: Account, recipient: Account, reposted_tweet: Tweet):
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
    sender: Account, recipient: Account, original_tweet: Tweet, reply: Tweet
):
    notification = create_notification(
        sender=sender,
        recipient=recipient,
        sender_tweet=reply,
        recipient_tweet=original_tweet,
        notification_type=NotificationType.REPLY,
    )
    return notification


def mark_notification_as_read(notifications_qs: QuerySet):
    pass
