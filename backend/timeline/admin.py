from django.contrib import admin
from .models import TimeLine

# Register your models here.

@admin.register(TimeLine)
class TimeLineAdmin(admin.ModelAdmin):
    list_display = ['id', 'tweet', 'referenced_tweet', 'tweet_author', 'tweet_type']

    def tweet_author(self, obj):
        return obj.tweet.author
    
    def tweet_type(self, obj):
        return obj.tweet.tweet_type
    
    def referenced_tweet(self, obj):
        return obj.tweet.referenced_tweet