from django.urls import path
from . import views



urlpatterns = [
    path("tweets/", views.SearchTweetResult.as_view(), name="search-tweets"),
    path("trends/", views.SearchTrendResult.as_view(), name="search-trends"),
]




