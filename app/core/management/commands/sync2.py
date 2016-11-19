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

        body_slug = Path(path).parent.parent.name
        meeting_time = parse_datetime(Path(path).parent.name.replace('.',':'))

        body, created = core.models.Body.objects.get_or_create(slug=body_slug, defaults={'name': data['name']})

        meeting, created = core.models.Meeting.objects.get_or_create(guid=data['id'][0:36], defaults={'json': data, 'body': body, 'time': meeting_time})

        return meeting
    else:
        return None


class Command(BaseCommand):
    args = '<dir>'
    help = 'Sample base command'


    def handle(self, *args, **options):
        print('Thanks for coming sync2!')

        documents_path = os.path.join(settings.MEDIA_ROOT, 'legistar')
        print(documents_path)

        for directory, directories, files in os.walk(documents_path, topdown=False):
            for name in files:
                path = os.path.join(directory, name)

                meeting = get_meeting_from(path)

                if name in ['agenda.pdf', 'minutes.pdf', ]:
                    print('agenda or minutes')
                    relpath = os.path.relpath(path, start=settings.MEDIA_ROOT)
                    path_md5 = getmd5(relpath)

                    doc, created = core.models.Document.objects.get_or_create(md5=path_md5, defaults={'meeting': meeting})
                    if created:
                        doc.original = relpath
                        doc.save()
        
                elif name == 'data.json':
                    print('data.json')
                    with open(path) as f:
                        data = json.load(f)
                    pprint(data)
                    
                    for agenda_item in data.get('agenda_items', []):
                        agenda_dir_name = '{}'.format(agenda_item['agenda_num'])
                        agenda_dir = os.path.join(os.path.dirname(path), agenda_dir_name)

                        agenda_item_obj, created = core.models.AgendaItem.objects.get_or_create(number= agenda_item.get('agenda_num', 0), meeting = meeting, defaults={'json': agenda_item, 'name': agenda_item['name'], 'description': agenda_item['title'] , 'version': agenda_item['version'] , 'type': agenda_item['type'], 'source_url': agenda_item['url'] })

                        for this_attachment in agenda_item.get('attachments', []):
                            attachment_path = os.path.join(agenda_dir, this_attachment['filename'])
                            relpath = os.path.relpath(attachment_path, start=settings.MEDIA_ROOT)
                            path_md5 = getmd5(relpath)

                            attachment_obj, created = core.models.Document.objects.get_or_create(md5=path_md5, defaults={'json': this_attachment, 'source_url': this_attachment['url']})

                            if created:
                                attachment_obj.original = relpath
                                attachment_obj.save()


