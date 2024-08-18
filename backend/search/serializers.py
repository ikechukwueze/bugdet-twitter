from rest_framework import serializers
from tweets.serializers import TweetSerializer




class ExtendedTweetSerializer(TweetSerializer):
    like_count = serializers.IntegerField(read_only=True)
    dislike_count = serializers.IntegerField(read_only=True)
    reply_count = serializers.IntegerField(read_only=True)
    reference_count = serializers.IntegerField(read_only=True)
    interactions = serializers.IntegerField(read_only=True)

    class Meta(TweetSerializer.Meta):
        fields = TweetSerializer.Meta.fields + [
            "like_count",
            "dislike_count",
            "reply_count",
            "reference_count",
            "interactions",
        ]
