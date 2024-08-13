from typing import Union
from datetime import datetime
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.timezone import make_aware
from .models import Account



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "username",
            "bio",
            "display_name",
            "profile_pic",
        ]
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        signup_date =  instance.signup_date
        output_format = "%B %Y"
        short_signup_date = datetime.strftime(signup_date, output_format)
        repr['short_signup_date'] = short_signup_date
        return repr


class AccountSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Account
        fields = [
            "email",
            "first_name",
            "last_name",
            "username",
            "password",
            "confirm_password",
        ]

    def validate(self, attrs: dict) -> Union[serializers.ValidationError, dict]:
        password = attrs["password"]
        confirm_password = attrs.pop("confirm_password")

        if not password == confirm_password:
            raise serializers.ValidationError({"password": "Passwords must match."})

        return attrs

    def create(self, validated_data):
        account = Account.objects.create_user(**validated_data)
        return account


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    account = AccountSerializer(read_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs: dict) -> Union[serializers.ValidationError, dict]:
        username = attrs.pop('username')
        password = attrs.pop('password')
        account = authenticate(username=username, password=password)
        if not account:
            raise serializers.ValidationError(
                {
                    "username": "Incorrect email or password",
                    "password": "Incorrect email or password.",
                }
            )
        if not account.is_active:
            raise serializers.ValidationError(
                {"email": "This account has been suspended."}
            )
        attrs["account"] = account
        attrs["token"] = account.get_token()
        return attrs
    
    def save(self, **kwargs):
        return self.validated_data
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        account_details = repr.pop('account')
        repr.update(account_details)
        return repr





class SimpleAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["username", "display_name", "profile_pic", "bio"]
