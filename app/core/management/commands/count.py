#!/usr/bin/env python

import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import core.models


class Command(BaseCommand):
    args = '<dir>'
    help = 'Counts objects'


    def handle(self, *args, **options):
        models = [core.models.Body, core.models.Document, core.models.Meeting, ]

        for this_model in models:
            count = this_model.objects.all().count()
            print('{}: {}'.format(this_model, count))
