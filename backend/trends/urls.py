from django.urls import path
from . import views



urlpatterns = [
    path("", views.TrendList.as_view(), name="trends-list"),
    path("<int:pk>/top-tweets/", views.TrendTopTweetsList.as_view(), name="top-trending-tweets"),
    path("<int:pk>/latest-tweets/", views.TrendLatestTweetsList.as_view(), name="latest-trending-tweets"),
]




