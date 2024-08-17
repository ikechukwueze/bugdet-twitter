from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from .serializers import TrendSerializer, SimpleTrendSerializer
from .models import Trend

# Create your views here.


class TrendList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    serializer_class = SimpleTrendSerializer
    queryset = Trend.objects.all()


class TrendTopTweetsList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    serializer_class = TrendSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Trend.objects.prefetch_related("tweets").filter(id=pk).order_by("-hits")


class TrendLatestTweetsList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    serializer_class = TrendSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        qs = (
            Trend.objects.prefetch_related("tweets")
            .filter(id=pk)
            .order_by("-tweets__created_at")
        )
        return qs
