"""Margins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as static_serve

from django.contrib.auth import views as auth_views

import core.views
import core.viewsets

from rest_framework import routers
from core import viewsets

from haystack.forms import FacetedSearchForm
from haystack.views import FacetedSearchView


urlpatterns = [
    url(r'^$', core.views.HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^body/(?P<guid>.*)$', core.views.BodyView.as_view(), name='body_details'),
    url(r'^document/(?P<guid>.*)$', core.views.DocumentView.as_view(), name='document_details'),
    url(r'^meeting/(?P<guid>.*)$', core.views.MeetingView.as_view(), name='meeting_details'),

    url(r'^agendaitem/(?P<guid>.*)$', core.views.AgendaItemView.as_view(), name='agendaitem_details'),


    url(r'^search/$', core.views.CustomFacetedSearchView.as_view(), name='haystack_search'),
]

router = routers.DefaultRouter()
router.register(r'document', core.viewsets.DocumentViewSet)
router.register(r'body', core.viewsets.BodyViewSet)
router.register(r'meeting', core.viewsets.MeetingViewSet)

urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += [
    url(r'^media/(?P<path>.*)$', static_serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^static/(?P<path>.*)$', static_serve, {
        'document_root': settings.STATIC_ROOT,
    }),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)