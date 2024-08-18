from django.urls import path
from . import views



urlpatterns = [
    path("", views.TrendList.as_view(), name="trends-list"),
]




