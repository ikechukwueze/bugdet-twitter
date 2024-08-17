from django.urls import path
from . import views



urlpatterns = [
    path("", views.TrendList.as_view(), name="trends-list"),
    path("<str:trend>/top-tweets/", views.TrendTopTweetsList.as_view(), name="top-trending-tweets"),
    path("<str:trend>/latest-tweets/", views.TrendLatestTweetsList.as_view(), name="latest-trending-tweets"),
]




