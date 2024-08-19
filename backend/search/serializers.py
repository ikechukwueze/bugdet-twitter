from rest_framework import serializers
from tweets.serializers import TweetSerializer




class ExtendedTweetSerializer(TweetSerializer):
    engagement = serializers.IntegerField(read_only=True)

    class Meta(TweetSerializer.Meta):
        fields = TweetSerializer.Meta.fields + [
            "engagement",
        ]
