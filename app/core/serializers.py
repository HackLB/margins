from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer
import core.search_indexes
import core.models


class DocumentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = core.models.Document
