from django.db import models
from accounts.models import Account
from tweets.models import Tweet

# Create your models here.


class NotificationType(models.TextChoices):
    FOLLOW = 'FOLLOW', 'FOLLOW'
    LIKE = 'LIKE', 'LIKE'
    DISLIKE = 'DISLIKE', 'DISLIKE'
    RETWEET = 'RETWEET', 'RETWEET'
    REPLY = 'REPLY', 'REPLY'
    QUOTE = 'QUOTE', 'QUOTE'
    MENTION = 'MENTION', 'MENTION'

class Notification(models.Model):
    sender = models.ForeignKey(Account, related_name='sent_notifications', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Account, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=10, choices=NotificationType.choices)
    tweet = models.ForeignKey(Tweet, related_name='notifications', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    # extra_data = models.JSONField(null=True, blank=True)  # For any extra data related to the notification

    def __str__(self):
        return f'{self.sender} {self.get_notification_type_display()} {self.recipient}'