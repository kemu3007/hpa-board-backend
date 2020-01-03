from rest_framework import viewsets

from .models import Application, Event
from .serializers import ApplicationSerializer, EventSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.filter(is_active=True)


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.filter(is_active=True)