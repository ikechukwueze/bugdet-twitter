from django.db.models import Count, F
from rest_framework import filters
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from tweets.models import Tweet
from .serializers import ExtendedTweetSerializer

# Create your views here.




class ExtendedSearchFilter(filters.SearchFilter):
    lookup_prefixes = {
        '^': 'istartswith',
        '=': 'iexact',
        '@': 'search',
        '$': 'iregex',
        '~': 'exact', # extension
    }



class SearchTweetResult(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    serializer_class = ExtendedTweetSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['author__username', 'content']
    ordering_fields = ['interactions', 'created_at']
    ordering = ['interactions']

    def get_queryset(self):
        qs = (
            Tweet.objects
            .annotate(
                like_count=Count("likes", distinct=True),
                dislike_count=Count("dislikes", distinct=True),
                reference_count=Count("referenced_tweets", distinct=True),
            )
            .annotate(
                interactions=F("like_count")
                + F("dislike_count")
                + F("reference_count")
            )
        )
        return qs



class SearchTrendResult(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    serializer_class = ExtendedTweetSerializer
    filter_backends = [ExtendedSearchFilter, filters.OrderingFilter]
    search_fields = ['~trends__phrase']
    ordering_fields = ['interactions', 'created_at']
    ordering = ['-interactions']

    def get_queryset(self):
        qs = (
            Tweet.objects
            .annotate(
                like_count=Count("likes", distinct=True),
                dislike_count=Count("dislikes", distinct=True),
                reference_count=Count("referenced_tweets", distinct=True),
            )
            .annotate(
                interactions=F("like_count")
                + F("dislike_count")
                + F("reference_count")
            )
        )
        return qs