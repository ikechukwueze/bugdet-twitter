from django.shortcuts import render, get_object_or_404
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import response, status
from accounts.models import Account
from notifications.models import NotificationType
from utils.helpers import create_follow_notification
from .models import Follower
from .serializers import FollowerSerializer, FollowingSerializer


# Create your views here.


class FollowUserView(APIView):
    def get_object(self, username):
        return get_object_or_404(Account, username=username)

    @transaction.atomic
    def post(self, request, username):
        account = self.get_object(username)
        if not account == self.request.user:
            Follower.objects.get_or_create(account=account, follower=self.request.user)
            create_follow_notification(self.request.user, account)
            return response.Response(status=status.HTTP_201_CREATED)
        return response.Response(
            {"error": "You can not follow yourself."},
            status=status.HTTP_400_BAD_REQUEST,
        )


class UnfollowUserView(APIView):
    def get_object(self, username):
        return get_object_or_404(Account, username=username)

    def post(self, request, username):
        account = self.get_object(username)
        try:
            following = Follower.objects.get(
                account=account, follower=self.request.user
            )
            following.delete()
        except Follower.DoesNotExist:
            pass
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class UserFollowersListView(ListAPIView):
    serializer_class = FollowerSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        followers = Follower.objects.filter(account__username=username)
        return followers


class UserFollowingListView(ListAPIView):
    serializer_class = FollowingSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        following = Follower.objects.filter(follower__username=username)
        return following



class UserFollowerCountView(APIView):
    def get_object(self, username):
        return get_object_or_404(Account, username=username)

    def get(self, request, username):
        account = self.get_object(username)
        count = Follower.objects.filter(account=account).count()
        return response.Response({'followers': count}, status=status.HTTP_200_OK)


class UserFollowingCountView(APIView):
    def get_object(self, username):
        return get_object_or_404(Account, username=username)

    def get(self, request, username):
        account = self.get_object(username)
        count = Follower.objects.filter(follower=account).count()
        return response.Response({'following': count}, status=status.HTTP_200_OK)