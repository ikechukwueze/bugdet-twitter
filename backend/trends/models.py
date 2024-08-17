from django.db import models
from tweets.models import Tweet

# Create your models here.


class Trend(models.Model):
    phrase = models.CharField(max_length=255, unique=True)
    tweets = models.ManyToManyField(Tweet, related_name='trends')
    hits = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phrase
    
    class Meta:
        ordering = ['-hits']
