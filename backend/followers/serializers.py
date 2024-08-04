from rest_framework import serializers
from accounts.serializers import SimpleAccountSerializer
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    follower = SimpleAccountSerializer(read_only=True)

    class Meta:
        model = Follower
        fields = ['follower']



class FollowingSerializer(serializers.ModelSerializer):
    account = SimpleAccountSerializer(read_only=True)

    class Meta:
        model = Follower
        fields = ['account']