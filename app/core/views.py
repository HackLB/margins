from django.conf import settings
from django.shortcuts import render, get_list_or_404, get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.db.models import Count
from django.contrib.auth.models import User, Group
from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from haystack.generic_views import SearchView
import core.models
import core.serializers


class HomeView(View):
    template = 'home.html'

    def __str__(self):
        return 'HomeView'

    def get(self, request):
        bodies = core.models.Body.objects.all().prefetch_related('meetings')
        documents = core.models.Document.objects.all()
        return render_to_response(self.template, {'bodies': bodies, 'documents': documents})


class DocumentView(View):
    template = 'document.html'

    def __str__(self):
        return 'DocumentView'

    def get(self, request, guid):
        this_document = get_object_or_404(core.models.Document, pk=guid)
        return render_to_response(self.template, {'this_document': this_document})


class MeetingView(View):
    template = 'meeting.html'

    def __str__(self):
        return 'MeetingView'

    def get(self, request, guid):
        this_meeting = get_object_or_404(core.models.Meeting, pk=guid)
        return render_to_response(self.template, {'this_meeting': this_meeting})


class BodyView(View):
    template = 'body.html'

    def __str__(self):
        return 'BodyView'

    def get(self, request, guid):
        this_body = get_object_or_404(core.models.Body, pk=guid)
        return render_to_response(self.template, {'this_body': this_body})


class AgendaItemView(View):
    template = 'agendaitem.html'

    def __str__(self):
        return 'AgendaItemView'

    def get(self, request, guid):
        agenda_item = get_object_or_404(core.models.AgendaItem, pk=guid)
        return render_to_response(self.template, {'agenda_item': agenda_item})


