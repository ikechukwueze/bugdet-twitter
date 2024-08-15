from rest_framework import serializers
from tweets.serializers import SimpleTweetSerializer
from accounts.serializers import SimpleAccountSerializer
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "sender",
            "recipient",
            "notification_type",
            "sender_tweet",
            "recipient_tweet",
            "created_at",
            "is_read",
        ]
        read_only_fields = ["id", "created_at"]



class SimpleNotificationSerializer(serializers.ModelSerializer):
    sender = SimpleAccountSerializer(read_only=True)
    recipient = SimpleAccountSerializer(read_only=True)
    sender_tweet = SimpleTweetSerializer(read_only=True)
    recipient_tweet = SimpleTweetSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = [
            "sender",
            "recipient",
            "notification_type",
            "sender_tweet",
            "recipient_tweet",
            "created_at",
            "is_read",
        ]
        read_only_fields = ["id", "created_at"]