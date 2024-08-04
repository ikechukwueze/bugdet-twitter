from django.db import models
from django.db.models import F, Q
from django.db.models.constraints import CheckConstraint
from accounts.models import Account

# Create your models here.


class Follower(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="followers")
    follower = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="following")

    class Meta:
        unique_together = ("account", "follower")
        constraints = [
            CheckConstraint(
                name="account_is_not_follower", check=~Q(account=F("follower"))
            ),
        ]
