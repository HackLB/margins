from django.contrib.auth.models import User, Group
from rest_framework import viewsets
import core.models
import core.serializers


class BodyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = core.models.Body.objects.all()
    serializer_class = core.serializers.BodySerializer



class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = core.models.Document.objects.all()
    serializer_class = core.serializers.DocumentSerializer



class MeetingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Meetings to be viewed or edited.
    """
    queryset = core.models.Meeting.objects.all()
    serializer_class = core.serializers.MeetingSerializer


class AgendaItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows meeting Agenda Items to be viewed or edited.
    """
    queryset = core.models.AgendaItem.objects.all()
    serializer_class = core.serializers.AgendaItemSerializer
