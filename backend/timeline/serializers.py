from rest_framework import serializers
from tweets.serializers import TweetSerializer, SimpleTweetSerializer
from .models import TimeLine


# class TimelineSerializer(serializers.ModelSerializer):
#     tweet = SimpleTweetSerializer(read_only=True)
#     like_count = serializers.IntegerField(read_only=True)
#     dislike_count = serializers.IntegerField(read_only=True)
#     reply_count = serializers.IntegerField(read_only=True)
#     repost_count = serializers.IntegerField(read_only=True)

#     class Meta:
#         model = TimeLine
#         fields = ["tweet", "like_count", "dislike_count", "reply_count", "repost_count"]


class TimelineSerializer(serializers.ModelSerializer):
    tweet = TweetSerializer(read_only=True)
    owner = serializers.CharField(read_only=True)

    class Meta:
        model = TimeLine
        fields = ["tweet", "owner"]
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        tweet_dict = repr.pop('tweet')
        repr.update(tweet_dict)
        return repr