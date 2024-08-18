from rest_framework import serializers
from .models import Trend


class SimpleTrendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trend
        fields = ["id", "phrase", "hits"]
