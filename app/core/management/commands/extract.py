#!/usr/bin/env python

import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import core.models

from pprint import pprint

import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def pdfparser(data):

    fp = file(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()

    print(data)


class Command(BaseCommand):
    args = '<dir>'
    help = 'Sample base command'


    def add_arguments(self, parser):
        parser.add_argument('pdf')

    def handle(self, *args, **options):
        print('Thanks for coming!')
        pprint(options)
        # pdfparser(sys.argv[1])
        pdfparser(options['pdf'])
