from rest_framework import serializers
from accounts.serializers import SimpleAccountSerializer
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    follower = SimpleAccountSerializer(read_only=True)
    is_following = serializers.BooleanField(read_only=True)

    class Meta:
        model = Follower
        fields = ['follower', 'is_following']
    
    # def to_representation(self, instance):
    #     repr = super().to_representation(instance)
    #     ret_dict = {}
    #     follower_details = repr.pop('follower')
    #     ret_dict.update(follower_details)
    #     return ret_dict



class FollowingSerializer(serializers.ModelSerializer):
    account = SimpleAccountSerializer(read_only=True)
    follows_back = serializers.CharField(read_only=True)

    class Meta:
        model = Follower
        fields = ['account', 'follows_back']
    
    # def to_representation(self, instance):
    #     repr = super().to_representation(instance)
    #     ret_dict = {}
    #     account_details = repr.pop('account')
    #     ret_dict.update(account_details)
    #     return ret_dict