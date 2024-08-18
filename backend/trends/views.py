from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from tweets.models import Tweet
from .serializers import SimpleTrendSerializer
from .models import Trend

# Create your views here.


class TrendList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    serializer_class = SimpleTrendSerializer
    queryset = Trend.objects.all()

