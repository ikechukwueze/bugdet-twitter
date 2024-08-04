from django.shortcuts import render
from rest_framework import views
from rest_framework import response
from rest_framework import status
from .models import Account
from .serializers import AccountSignUpSerializer, LoginSerializer#, FollowAccountSerializer

# Create your views here.



class AccountSignUpView(views.APIView):
    authentication_classes = []

    def post(self, request):
        serializer = AccountSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        account_details = {
            "first_name": account.first_name,
            "last_name": account.last_name,
            "email": account.email,
            "username": account.username
        }
        return response.Response(account_details, status=status.HTTP_201_CREATED)


class AccountLoginView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.validated_data["account"]
        account_details = {
            "email": account.email,
            "token": account.get_token(),
        }
        return response.Response(account_details, status=status.HTTP_200_OK)


# class FollowAccountView(views.APIView):
#     def post(self, request):
#         serializer = FollowAccountSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         username = serializer.validated_data['username']
#         account_to_follow = Account.objects.get(username=username)
#         self.request.user.following.add(account_to_follow)
#         return response.Response(status=status.HTTP_201_CREATED)
    


# class UnfollowAccountView(views.APIView):
#     def post(self, request):
#         serializer = FollowAccountSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         username = serializer.validated_data['username']
#         account_to_unfollow = Account.objects.get(username=username)
#         self.request.user.following.remove(account_to_unfollow)
#         return response.Response(status=status.HTTP_201_CREATED)