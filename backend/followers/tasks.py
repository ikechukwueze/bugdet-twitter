from celery import shared_task
from utils.helpers import create_notification
from notifications.models import NotificationType
from accounts.models import Account


@shared_task()
def create_follow_notification(sender: Account, recipient: Account):
    notification = create_notification(
        sender=sender,
        recipient=recipient,
        recipient_tweet=None,
        sender_tweet=None,
        notification_type=NotificationType.FOLLOW,
    )
    return notification