from django.urls import path
from . import views



urlpatterns = [
    path("post/", views.PostTweetView.as_view(), name="post-tweet"),

    path("<int:tweet_id>/detail/", views.TweetDetailView.as_view(), name="tweet-detail"),
    path("<int:tweet_id>/delete/", views.DeleteTweetView.as_view(), name="delete-tweet"),
    path("<int:tweet_id>/replies/", views.TweetRepliesView.as_view(), name="tweet-replies"),

    path("<int:tweet_id>/reply/", views.ReplyTweetView.as_view(), name="reply-tweet"),
    path("<int:tweet_id>/quote/", views.QuoteTweetView.as_view(), name="quote-tweet"),
    path("<int:tweet_id>/retweet/", views.RetweetView.as_view(), name="retweet"),
    
    path("<int:tweet_id>/like/", views.LikeTweetView.as_view(), name="like-tweet"),
    path("<int:tweet_id>/dislike/", views.DislikeTweetView.as_view(), name="dislike-tweet"),

    path("<int:tweet_id>/like-count/", views.TweetLikeCountView.as_view(), name="tweet-like-count"),
    path("<int:tweet_id>/dislike-count/", views.TweetDisLikeCountView.as_view(), name="tweet-dislike-count"),
    path("<int:tweet_id>/repost-count/", views.TweetRepostCountView.as_view(), name="tweet-repost-count"),
    path("<int:tweet_id>/retweet-count/", views.TweetRetweetCountView.as_view(), name="tweet-retweet-count"),
    path("<int:tweet_id>/quote-count/", views.TweetQuoteCountView.as_view(), name="tweet-quote-count"),
    path("<int:tweet_id>/reply-count/", views.TweetReplyCountView.as_view(), name="tweet-reply-count"),

    path("<int:tweet_id>/like-status/", views.TweetLikeStatusView.as_view(), name="tweet-like-status"),
    path("<int:tweet_id>/dislike-status/", views.TweetDislikeStatusView.as_view(), name="tweet-dislike-status"),
    path("<int:tweet_id>/quote-status/", views.TweetQuoteStatusView.as_view(), name="tweet-quote-status"),
    path("<int:tweet_id>/retweet-status/", views.TweetRetweetStatusView.as_view(), name="tweet-retweet-status"),

    path("<str:username>/", views.UserTweetsView.as_view(), name="user-tweets"),
    path("<str:username>/replies/", views.UserRepliesView.as_view(), name="user-replies"),
    path("<str:username>/quotes/", views.UserQuotesView.as_view(), name="user-quotes"),
    path("<str:username>/retweets/", views.UserRetweetsView.as_view(), name="user-retweets"),
    path("<str:username>/liked-tweets/", views.UserLikedTweetsView.as_view(), name="user-liked-tweets"),
    path("<str:username>/disliked-tweets/", views.UserDislikedTweetsView.as_view(), name="user-disliked-tweets"),
]




