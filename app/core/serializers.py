from rest_framework import serializers
import core.search_indexes
import core.models


class DocumentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = core.models.Document
        fields = '__all__'


class BodySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = core.models.Body
        fields = '__all__'


class MeetingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = core.models.Meeting
        fields = '__all__'


class AgendaItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = core.models.AgendaItem
        fields = '__all__'
