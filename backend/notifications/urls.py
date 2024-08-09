from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotificationListView.as_view(), name='notification-list'),
    path('count/', views.NotificationCountView.as_view(), name='notification-count'),
    path('<int:pk>/read/', views.MarkNotificationAsReadView.as_view(), name='mark-notification-as-read'),
]
