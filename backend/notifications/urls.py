from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotificationListView.as_view(), name='notification-list'),
    path('current/', views.CurrentNotificationListView.as_view(), name='current-notification-list'),
    path('count/', views.NotificationCountView.as_view(), name='notification-count'),
    path('<int:pk>/mark-as-read/', views.MarkNotificationAsReadView.as_view(), name='mark-notification-as-read'),
]
