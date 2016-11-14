#!/usr/bin/env python

import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from pathlib import Path
from pprint import pprint
import hashlib
import simplejson as json
from django.utils.dateparse import parse_datetime
import core.models


def getmd5(message):    
    """
    Returns MD5 hash of string passed to it.
    """
    return hashlib.md5(message.encode('utf-8')).hexdigest()


def get_meeting_from(path):
    data_json = (Path(path).parent / 'data.json').as_posix()


    if os.path.exists(data_json):

        with open(data_json) as f:
            data = json.load(f)
            pprint(data)

        body_slug = Path(path).parent.parent.name
        meeting_time = parse_datetime(Path(path).parent.name.replace('.',':'))

        body, created = core.models.Body.objects.get_or_create(slug=body_slug, defaults={'name': data['name']})
        pprint(body)

        meeting, created = core.models.Meeting.objects.get_or_create(guid=data['id'][0:36], defaults={'json': data, 'body': body, 'time': meeting_time})

        return meeting
    else:
        return None


class Command(BaseCommand):
    args = '<dir>'
    help = 'Sample base command'


    def handle(self, *args, **options):
        print('Thanks for coming!')

        documents_path = os.path.join(settings.MEDIA_ROOT, 'legistar')
        print(documents_path)

        for directory, directories, files in os.walk(documents_path, topdown=False):
            for name in files:
                if name in ['agenda.pdf', 'minutes.pdf', ]:

                    path = os.path.join(directory, name)
                    meeting = get_meeting_from(path)
                    relpath = os.path.relpath(path, start=settings.MEDIA_ROOT)
                    path_md5 = getmd5(relpath)

                    doc, created = core.models.Document.objects.get_or_create(md5=path_md5, defaults={'meeting': meeting})
                    if created:
                        doc.original = relpath
                        doc.save()