from accounts.models import Account
from django.db import models

# Create your models here.


class TweetType(models.TextChoices):
    TWEET = 'TWEET', 'TWEET'
    RETWEET = 'RETWEET', 'RETWEET'
    REPLY = 'REPLY', 'REPLY'
    QUOTE = 'QUOTE', 'QUOTE'


class Tweet(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='tweets')
    content = models.TextField(max_length=280, blank=True)
    tweet_type = models.CharField(max_length=10, choices=TweetType.choices, default=TweetType.TWEET)
    referenced_tweet = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='referenced_tweets')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content[:50]
    
    class Meta:
        ordering = ['created_at']



class LikedTweet(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='liked_tweets')
    referenced_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['account', 'referenced_tweet']


class DislikedTweet(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='disliked_tweets')
    referenced_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='dislikes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['account', 'referenced_tweet']
