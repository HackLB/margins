#!/usr/bin/env python

import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import core.models

class Command(BaseCommand):
    args = '<dir>'
    help = 'Sample base command'


    def handle(self, *args, **options):
        print('Thanks for coming!')

