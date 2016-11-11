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
        documents = core.models.Document.objects.all()
        return render_to_response(self.template, {'documents': documents})


class DocumentView(View):
    template = 'pdf.html'

    def __str__(self):
        return 'DocumentView'

    def get(self, request, guid):
        this_document = get_object_or_404(core.models.Document, pk=guid)
        return render_to_response(self.template, {'this_document': this_document})