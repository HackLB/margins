#!/usr/bin/env python

import PyPDF2
import sys, os


class PDF(object):
    """
    An interface for PDF files.
    Pass it the path to a PDF. Access properties such as PDF.text and PDF.pages
    """

    path = None

    def __init__(self, path):
        self.path = path

    @property
    def text(self):
        try:
            with open(self.path, 'rb') as pdfFileObj:
                pdfr = PyPDF2.PdfFileReader(pdfFileObj)
                return '\n\n'.join([pdfr.getPage(x).extractText() for x in range(0, pdfr.numPages)])
        except:
            return None

    @property
    def pages(self):
        with open(self.path, 'rb') as pdfFileObj:
            return PyPDF2.PdfFileReader(pdfFileObj).numPages


if __name__ == "__main__":
    path = sys.argv[1]
    print(path)

    pdf_obj = PDF(path)

    print(pdf_obj.text)
    print(pdf_obj.pages)
    # sys.argv[1]