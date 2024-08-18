from rest_framework import serializers
from accounts.serializers import SimpleAccountSerializer
from utils.helpers import reformat_tweet_timestamp
from .models import Tweet




class SimpleTweetSerializer(serializers.ModelSerializer):
    author = SimpleAccountSerializer(read_only=True)
    # tweet_type = serializers.CharField(read_only=True)
    
    class Meta:
        model = Tweet
        exclude = ['referenced_tweet', 'tweet_type']
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr["created_at"] = reformat_tweet_timestamp(repr["created_at"])
        return repr


class ReferencedTweetSerializer(serializers.ModelSerializer):
    author = SimpleAccountSerializer(read_only=True)

    class Meta:
        model = Tweet
        exclude = ['referenced_tweet', 'tweet_type']
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr["created_at"] = reformat_tweet_timestamp(repr["created_at"])
        return repr


class TweetSerializer(serializers.ModelSerializer):
    author = SimpleAccountSerializer(read_only=True)
    referenced_tweet = ReferencedTweetSerializer(read_only=True)
    tweet_type = serializers.CharField(read_only=True)
    
    class Meta:
        model = Tweet
        fields = ['id', 'author', 'content', 'tweet_type', 'referenced_tweet', 'created_at']
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr["created_at"] = reformat_tweet_timestamp(repr["created_at"])
        return repr


class ReplyTweetSerializer(serializers.ModelSerializer):
    author = SimpleAccountSerializer(read_only=True)
    referenced_tweet = ReferencedTweetSerializer(read_only=True)
    tweet_type = serializers.CharField(read_only=True)
    tweet_id = serializers.IntegerField(write_only=True)
    content = serializers.CharField(min_length=1)

    class Meta:
        model = Tweet
        fields = '__all__'
    
    def validate(self, attrs):
        tweet_id = attrs.pop('tweet_id')
        
        try:
            referenced_tweet = Tweet.objects.get(id=tweet_id)
        except Tweet.DoesNotExist:
            raise serializers.ValidationError('Tweet does not exist')

        attrs['referenced_tweet'] = referenced_tweet
        return attrs


class QuoteTweetSerializer(ReplyTweetSerializer):
    pass







