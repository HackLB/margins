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


urlpatterns = [
    url(r'^$', core.views.HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^document/(?P<guid>.*)$', core.views.DocumentView.as_view(), name='document_details'),

]

router = routers.DefaultRouter()
router.register(r'document', core.viewsets.DocumentViewSet)
urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]