from django.contrib.auth.models import User, Group
from rest_framework import viewsets
import core.models
import core.serializers


class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = core.models.Document.objects.all()
    serializer_class = core.serializers.DocumentSerializer
