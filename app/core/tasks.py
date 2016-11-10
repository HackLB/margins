from __future__ import absolute_import

from celery import shared_task
from django.conf import settings


@shared_task
def echo(value):
    return value
