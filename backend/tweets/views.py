from django.shortcuts import get_object_or_404
from django.db import transaction
from django.db.models import Q
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, response
from utils.helpers import (
    push_tweet_to_timeline,
    push_tweet_to_followers,
    create_mention_notification,
    create_like_notification,
    create_dislike_notification,
    create_reply_notification,
    create_quote_notification,
    create_retweet_notification,
)
from .serializers import TweetSerializer, ReplyTweetSerializer, QuoteTweetSerializer
from .models import Tweet, TweetType, LikedTweet, DislikedTweet
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class PostTweetView(APIView):

    @transaction.atomic
    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tweet = serializer.save(author=self.request.user, tweet_type=TweetType.TWEET)
        push_tweet_to_timeline(tweet)
        push_tweet_to_followers(self.request.user, tweet)
        create_mention_notification(self.request.user, tweet)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class ReplyTweetView(APIView):

    @transaction.atomic
    def post(self, request, tweet_id):
        content = request.data.get("content", "")
        data = {"content": content.strip(), "tweet_id": tweet_id}
        serializer = ReplyTweetSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        tweet = serializer.save(author=self.request.user, tweet_type=TweetType.REPLY)
        push_tweet_to_timeline(tweet)
        push_tweet_to_followers(self.request.user, tweet)
        create_reply_notification(
            sender=self.request.user,
            recipient=tweet.referenced_tweet.author,
            reply=tweet,
            original_tweet=tweet.referenced_tweet,
        )
        create_mention_notification(self.request.user, tweet)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class QuoteTweetView(APIView):

    @transaction.atomic
    def post(self, request, tweet_id):
        content = request.data.get("content", "")
        data = {"content": content.strip(), "tweet_id": tweet_id}
        serializer = QuoteTweetSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        tweet = serializer.save(author=self.request.user, tweet_type=TweetType.QUOTE)
        push_tweet_to_timeline(tweet)
        push_tweet_to_followers(self.request.user, tweet)
        create_quote_notification(
            sender=self.request.user,
            recipient=tweet.referenced_tweet.author,
            quoted_tweet=tweet.referenced_tweet,
            quote=tweet,
        )
        create_mention_notification(self.request.user, tweet)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class RetweetView(APIView):
    def get_object(self, tweet_id):
        return get_object_or_404(Tweet, id=tweet_id)

    @transaction.atomic
    def post(self, request, tweet_id):
        account = self.request.user
        tweet = self.get_object(tweet_id)
        retweet, created = Tweet.objects.get_or_create(
            author=account,
            referenced_tweet=tweet,
            tweet_type=TweetType.RETWEET,
        )
        if not created:
            retweet.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)

        push_tweet_to_timeline(retweet)
        push_tweet_to_followers(account, retweet)
        create_retweet_notification(
            sender=account, recipient=tweet.author, reposted_tweet=tweet
        )
        return response.Response(status=status.HTTP_201_CREATED)


class TweetDetailView(RetrieveAPIView):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()
    lookup_url_kwarg = "tweet_id"


class DeleteTweetView(DestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    serializer_class = TweetSerializer
    queryset = Tweet.objects.select_related("author").all()
    lookup_url_kwarg = "tweet_id"


class TweetRepliesView(ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        tweet_id = self.kwargs["tweet_id"]
        return Tweet.objects.filter(
            referenced_tweet__id=tweet_id, tweet_type=TweetType.REPLY
        )


class UserTweetsView(ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        return Tweet.objects.filter(
            author__username=username, tweet_type=TweetType.TWEET
        )


class UserRepliesView(ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        return Tweet.objects.filter(
            author__username=username, tweet_type=TweetType.REPLY
        )


class UserQuotesView(ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        return Tweet.objects.filter(
            author__username=username, tweet_type=TweetType.QUOTE
        )


class UserRetweetsView(ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        return Tweet.objects.filter(
            author__username=username, tweet_type=TweetType.RETWEET
        )


class UserLikedTweetsView(ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        return Tweet.objects.filter(likes__account__username=username)


class UserDislikedTweetsView(ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        return Tweet.objects.filter(dislikes__account__username=username)


class LikeTweetView(APIView):
    def get_object(self, tweet_id):
        return get_object_or_404(Tweet, id=tweet_id)

    def undislike_tweet(self, tweet):
        try:
            disliked_tweet = DislikedTweet.objects.get(
                account=self.request.user, referenced_tweet=tweet
            )
            disliked_tweet.delete()
        except DislikedTweet.DoesNotExist:
            pass

    @transaction.atomic
    def post(self, request, tweet_id):
        account = self.request.user
        tweet = self.get_object(tweet_id)
        liked_tweet_author = tweet.author
        self.undislike_tweet(tweet)
        liked_tweet, created = LikedTweet.objects.get_or_create(
            account=account, referenced_tweet=tweet
        )

        if not created:
            liked_tweet.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)

        if not account == liked_tweet.referenced_tweet.author:
            create_like_notification(
                sender=account, recipient=liked_tweet_author, liked_tweet=tweet
            )

        return response.Response(status=status.HTTP_201_CREATED)


class DislikeTweetView(APIView):
    def get_object(self, tweet_id):
        return get_object_or_404(Tweet, id=tweet_id)

    def unlike_tweet(self, tweet):
        try:
            liked_tweet = LikedTweet.objects.get(
                account=self.request.user, referenced_tweet=tweet
            )
            liked_tweet.delete()
        except LikedTweet.DoesNotExist:
            pass

    @transaction.atomic
    def post(self, request, tweet_id):
        account = self.request.user
        tweet = self.get_object(tweet_id)
        disliked_tweet_author = tweet.author
        self.unlike_tweet(tweet)
        disliked_tweet, created = DislikedTweet.objects.get_or_create(
            account=account, referenced_tweet=tweet
        )
        if not created:
            disliked_tweet.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)

        if not account == disliked_tweet.referenced_tweet.author:
            create_dislike_notification(
                sender=account, recipient=disliked_tweet_author, disliked_tweet=tweet
            )

        return response.Response(status=status.HTTP_201_CREATED)


### Tweet stat counts


class TweetLikeCountView(APIView):
    def get_object(self, tweet_id):
        return get_object_or_404(Tweet, id=tweet_id)

    @transaction.atomic
    def get(self, request, tweet_id):
        tweet = self.get_object(tweet_id)
        like_count = LikedTweet.objects.filter(referenced_tweet=tweet).count()
        return response.Response({"like_count": like_count}, status=status.HTTP_200_OK)


class TweetDisLikeCountView(APIView):
    def get_object(self, tweet_id):
        return get_object_or_404(Tweet, id=tweet_id)

    @transaction.atomic
    def get(self, request, tweet_id):
        tweet = self.get_object(tweet_id)
        dislike_count = DislikedTweet.objects.filter(referenced_tweet=tweet).count()
        return response.Response(
            {"dislike_count": dislike_count}, status=status.HTTP_200_OK
        )


class TweetReplyCountView(APIView):
    def get_object(self, tweet_id):
        return get_object_or_404(Tweet, id=tweet_id)

    @transaction.atomic
    def get(self, request, tweet_id):
        tweet = self.get_object(tweet_id)
        reply_count = Tweet.objects.filter(
            referenced_tweet=tweet, tweet_type=TweetType.REPLY
        ).count()
        return response.Response(
            {"reply_count": reply_count}, status=status.HTTP_200_OK
        )


class TweetRepostCountView(APIView):
    def get_object(self, tweet_id):
        return get_object_or_404(Tweet, id=tweet_id)

    @transaction.atomic
    def get(self, request, tweet_id):
        tweet = self.get_object(tweet_id)
        ref_tweet = Q(referenced_tweet=tweet)
        reposted = Q(tweet_type=TweetType.QUOTE) | Q(tweet_type=TweetType.RETWEET)
        repost_count = Tweet.objects.filter(ref_tweet, reposted).count()
        return response.Response(
            {"repost_count": repost_count}, status=status.HTTP_200_OK
        )


class TweetQuoteCountView(APIView):
    def get_object(self, tweet_id):
        return get_object_or_404(Tweet, id=tweet_id)

    @transaction.atomic
    def get(self, request, tweet_id):
        tweet = self.get_object(tweet_id)
        quote_count = Tweet.objects.filter(
            referenced_tweet=tweet, tweet_type=TweetType.QUOTE
        ).count()
        return response.Response(
            {"quote_count": quote_count}, status=status.HTTP_200_OK
        )


class TweetRetweetCountView(APIView):
    def get_object(self, tweet_id):
        return get_object_or_404(Tweet, id=tweet_id)

    @transaction.atomic
    def get(self, request, tweet_id):
        tweet = self.get_object(tweet_id)
        retweet_count = Tweet.objects.filter(
            referenced_tweet=tweet, tweet_type=TweetType.RETWEET
        ).count()
        return response.Response(
            {"retweet_count": retweet_count}, status=status.HTTP_200_OK
        )


# Tweet status


class TweetLikeStatusView(APIView):
    def get_object(self, tweet_id):
        return get_object_or_404(Tweet, id=tweet_id)

    @transaction.atomic
    def get(self, request, tweet_id):
        account = self.request.user
        tweet = self.get_object(tweet_id)
        liked_status = LikedTweet.objects.filter(
            account=account, referenced_tweet=tweet
        ).exists()
        return response.Response({"is_liked": liked_status}, status=status.HTTP_200_OK)


class TweetDislikeStatusView(APIView):
    def get_object(self, tweet_id):
        return get_object_or_404(Tweet, id=tweet_id)

    @transaction.atomic
    def get(self, request, tweet_id):
        account = self.request.user
        tweet = self.get_object(tweet_id)
        disliked_status = DislikedTweet.objects.filter(
            account=account, referenced_tweet=tweet
        ).exists()
        return response.Response(
            {"is_disliked": disliked_status}, status=status.HTTP_200_OK
        )


class TweetRetweetStatusView(APIView):
    def get_object(self, tweet_id):
        return get_object_or_404(Tweet, id=tweet_id)

    @transaction.atomic
    def get(self, request, tweet_id):
        account = self.request.user
        tweet = self.get_object(tweet_id)
        retweet_status = Tweet.objects.filter(
            author=account, referenced_tweet=tweet, tweet_type=TweetType.RETWEET
        ).exists()
        return response.Response(
            {"is_retweeted": retweet_status}, status=status.HTTP_200_OK
        )


class TweetQuoteStatusView(APIView):
    def get_object(self, tweet_id):
        return get_object_or_404(Tweet, id=tweet_id)

    @transaction.atomic
    def get(self, request, tweet_id):
        account = self.request.user
        tweet = self.get_object(tweet_id)
        quote_status = Tweet.objects.filter(
            author=account, referenced_tweet=tweet, tweet_type=TweetType.QUOTE
        ).exists()
        return response.Response({"is_quoted": quote_status}, status=status.HTTP_200_OK)
