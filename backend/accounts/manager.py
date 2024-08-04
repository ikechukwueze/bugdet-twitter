from django.contrib.auth.models import BaseUserManager
from django.db.models import Model
from django.db import transaction
from rest_framework.authtoken.models import Token



class AccountManager(BaseUserManager):
    
    @transaction.atomic
    def create_user(
        self,
        email: str,
        first_name: str,
        last_name: str,
        username: str,
        password: str = None
    ) -> Model:
        """
        The create user model manager method, creates a user account
        with specified details.
        """
        if not email.strip():
            raise ValueError("Email must be provided.")

        if not first_name.strip():
            raise ValueError("First name must be provided.")

        if not last_name.strip():
            raise ValueError("Last name must be provided.")

        if not username.strip():
            raise ValueError("Role must be provided.")

        account = self.model(
            email=self.normalize_email(email.strip()),
            first_name=first_name.strip(),
            last_name=last_name.strip(),
            username=username.strip()
        )
        account.set_password(password)
        account.save(using=self._db)
        account.followers.add(account)
        self.create_token(account)
        return account

    def create_superuser(
        self,
        email: str,
        first_name: str,
        last_name: str,
        username: str,
        password: str,
    ) -> Model:
        
        account = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )
        account.is_admin = True
        account.save(using=self._db)
        account.followers.add(account)
        return account
    
    def create_token(self, account: Model):
        Token.objects.get_or_create(user=account)