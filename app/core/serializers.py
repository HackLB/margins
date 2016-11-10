from rest_framework import serializers
import core.search_indexes
import core.models


class DocumentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = core.models.Document
