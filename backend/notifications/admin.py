from django.contrib import admin
from .models import Notification
# Register your models here.



@admin.register(Notification)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ['sender', 'recipient', 'notification_type']
    list_filter = ['notification_type']