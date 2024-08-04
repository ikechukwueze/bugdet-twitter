from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "recipient",
            "sender",
            "notification_type",
            "tweet",
            "created_at",
            "is_read",
        ]
        read_only_fields = ["id", "created_at"]
