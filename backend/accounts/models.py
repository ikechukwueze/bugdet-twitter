import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from rest_framework.authtoken.models import Token
from django_resized import ResizedImageField
from .manager import AccountManager



class Account(AbstractBaseUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=15, unique=True, db_index=True)
    email = models.CharField(max_length=100, unique=True, db_index=True)
    display_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=100, blank=True)
    profile_pic = ResizedImageField(
        size=[300, 300],
        crop=['middle', 'center'],
        upload_to='profile_pictures/',
        blank=True,
        null=True,
        default='profile_pictures/default_profile_pic.jpg'
    )
    signup_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]


    def __str__(self):
        return self.username


    def has_perm(self, perm, obj=None):
        return True


    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self) -> bool:
        return self.is_admin
    

    def get_token(self) -> str:
        token = Token.objects.get(user=self).key
        return token

    # def follow(self, account):
    #     self.following.add(account)
    
    # def unfollow(self, account):
    #     self.following.remove(account)
    
    # def block(self, account):
    #     self.blocked_accounts.add(account)
    
    # def unblock(self, account):
    #     self.blocked_accounts.remove(account)