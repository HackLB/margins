#!/usr/bin/env python

import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import hashlib

import core.models

def getmd5(message):    
    """
    Returns MD5 hash of string passed to it.
    """
    return hashlib.md5(message.encode('utf-8')).hexdigest()



class Command(BaseCommand):
    args = '<dir>'
    help = 'Sample base command'


    def handle(self, *args, **options):
        print('Thanks for coming!')

        documents_path = os.path.join(settings.MEDIA_ROOT, 'legistar')
        print(documents_path)

        for directory, directories, files in os.walk(documents_path, topdown=False):
            for name in files:
                if name.endswith('.pdf'):
                    path = os.path.join(directory, name)
                    relpath = os.path.relpath(path, start=settings.MEDIA_ROOT)
                    path_md5 = getmd5(relpath)
                    print(relpath)

                    doc, created = core.models.Document.objects.get_or_create(md5=path_md5)
                    if created:
                        doc.original = relpath
                        doc.save()