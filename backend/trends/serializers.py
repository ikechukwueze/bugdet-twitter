from rest_framework import serializers
from tweets.serializers import TweetSerializer
from .models import Trend



class SimpleTrendSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trend
        fields = ['id', 'phrase', 'hits']


class TrendSerializer(serializers.ModelSerializer):
    tweets = TweetSerializer(many=True)

    class Meta:
        model = Trend
        fields = ['phrase', 'tweets', 'likes', 'dislikes']