from rest_framework import serializers
from tweets.serializers import SimpleTweetSerializer
from accounts.serializers import SimpleAccountSerializer
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "recipient",
            "sender",
            "notification_type",
            "tweet",
            "created_at",
            "is_read",
        ]
        read_only_fields = ["id", "created_at"]



class SimpleNotificationSerializer(serializers.ModelSerializer):
    recipient = SimpleAccountSerializer(read_only=True)
    sender = SimpleAccountSerializer(read_only=True)
    tweet = SimpleTweetSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = [
            "recipient",
            "sender",
            "notification_type",
            "tweet",
            "created_at",
            "is_read",
        ]
        read_only_fields = ["id", "created_at"]