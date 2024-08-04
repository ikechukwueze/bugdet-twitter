from rest_framework.generics import ListAPIView, UpdateAPIView
from .models import Notification
from .serializers import NotificationSerializer




class NotificationListView(ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)


class MarkNotificationAsReadView(UpdateAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def perform_update(self, serializer):
        serializer.instance.is_read = True
        serializer.save()
