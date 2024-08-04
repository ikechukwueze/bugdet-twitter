from django.contrib import admin
from .models import Tweet, LikedTweet, DislikedTweet
# Register your models here.



@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_filter = ['tweet_type']
    list_display = ['author', 'tweet_type', 'content', 'referenced_tweet', 'id']
    # readonly_fields = ['referenced_tweet']


@admin.register(LikedTweet)
class LikedTweetAdmin(admin.ModelAdmin):
    pass


@admin.register(DislikedTweet)
class DislikedTweetAdmin(admin.ModelAdmin):
    pass