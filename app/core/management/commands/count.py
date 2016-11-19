#!/usr/bin/env python

from django.core.management.base import BaseCommand, CommandError
import django.apps

class Command(BaseCommand):
    help = 'Counts model instances'

    def handle(self, *args, **options):
        for this_model in django.apps.apps.get_models():
            count = this_model.objects.all().count()
            print('{}: {}'.format(this_model, count))
            