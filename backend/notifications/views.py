from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework import views, status, response
from .models import Notification
from .serializers import NotificationSerializer


class NotificationListView(ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)


class NotificationCountView(views.APIView):
    def get(self, request):
        account = self.request.user
        notification_count = (
            Notification.objects
            .filter(recipient=account, is_read=False)
            .count()
        )
        return response.Response(
            {"notification_count": notification_count}, status.HTTP_200_OK
        )


class MarkNotificationAsReadView(UpdateAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def perform_update(self, serializer):
        serializer.instance.is_read = True
        serializer.save()
