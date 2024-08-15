from rest_framework.generics import ListAPIView
from .serializers import TimelineSerializer
from .models import TimeLine


# Create your views here.


class HomeTimelineView(ListAPIView):
    serializer_class = TimelineSerializer

    def get_queryset(self):
        queryset = (
            TimeLine.objects.select_related("tweet__author", "tweet__referenced_tweet")
            .filter(viewers=self.request.user)
            .order_by("-tweet__created_at")
        )
        return queryset


class UserTimelineView(ListAPIView):
    serializer_class = TimelineSerializer

    def get_queryset(self):
        username = self.kwargs.get("username")
        queryset = TimeLine.objects.filter(tweet__author__username=username).order_by(
            "-created_at"
        )
        return queryset
