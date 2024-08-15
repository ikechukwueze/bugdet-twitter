from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework import views, status, response
from django.utils import timezone
from .models import Notification
from .serializers import NotificationSerializer, SimpleNotificationSerializer


class CurrentNotificationListView(ListAPIView):
    serializer_class = SimpleNotificationSerializer

    def get_queryset(self):
        today = timezone.datetime.today().date()
        qs = (
            Notification.objects
            .filter(recipient=self.request.user, created_at__date=today)
            .order_by("-created_at")
        )
        return qs


class NotificationListView(ListAPIView):
    serializer_class = SimpleNotificationSerializer

    def get_queryset(self):
        qs = (
            Notification.objects
            .filter(recipient=self.request.user)
            .order_by("-created_at")
        )
        qs.update(is_read=True)
        return qs


class NotificationCountView(views.APIView):
    def get(self, request):
        account = self.request.user
        notification_count = (
            Notification.objects
            .filter(recipient=account, is_read=False)
            .count()
        )
        return response.Response({"notification_count": notification_count}, status.HTTP_200_OK)


class MarkNotificationAsReadView(UpdateAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def perform_update(self, serializer):
        serializer.instance.is_read = True
        serializer.save()
