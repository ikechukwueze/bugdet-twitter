from django.urls import path
from . import views



urlpatterns = [
    path("home/", views.HomeTimelineView.as_view(), name="home-timeline"),
    path("users/<str:username>/timeline/", views.UserTimelineView.as_view(), name="user-timeline"),
]




