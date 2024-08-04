from django.db import models
from accounts.models import Account
from tweets.models import Tweet

# Create your models here.


class TimeLine(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='timeline')
    viewers = models.ManyToManyField(Account)