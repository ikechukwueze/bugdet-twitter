from django.db.models import Count, F
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from tweets.models import Tweet
from .serializers import TrendTweetSerializer, SimpleTrendSerializer
from .models import Trend

# Create your views here.


class TrendList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    serializer_class = SimpleTrendSerializer
    queryset = Trend.objects.all()


class TrendTopTweetsList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    serializer_class = TrendTweetSerializer

    def get_queryset(self):
        trend = self.kwargs["trend"]
        qs = (
            Tweet.objects.filter(trends__phrase=trend)
            .annotate(
                like_count=Count("likes", distinct=True),
                dislike_count=Count("dislikes", distinct=True),
                reference_count=Count("referenced_tweets", distinct=True),
            )
            .annotate(
                interaction_count=F("like_count")
                + F("dislike_count")
                + F("reference_count")
            )
            .order_by("-interaction_count")
        )
        return qs


class TrendLatestTweetsList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    serializer_class = TrendTweetSerializer

    def get_queryset(self):
        trend = self.kwargs["trend"]
        qs = Tweet.objects.filter(trends__phrase=trend).order_by("-created_at")
        return qs
