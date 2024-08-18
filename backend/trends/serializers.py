from rest_framework import serializers
from tweets.serializers import TweetSerializer
from .models import Trend


class SimpleTrendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trend
        fields = ["id", "phrase", "hits"]


class TrendTweetSerializer(TweetSerializer):
    like_count = serializers.IntegerField(read_only=True)
    dislike_count = serializers.IntegerField(read_only=True)
    reply_count = serializers.IntegerField(read_only=True)
    reference_count = serializers.IntegerField(read_only=True)
    interaction_count = serializers.IntegerField(read_only=True)

    class Meta(TweetSerializer.Meta):
        fields = TweetSerializer.Meta.fields + [
            "like_count",
            "dislike_count",
            "reply_count",
            "reference_count",
            "interaction_count",
        ]
