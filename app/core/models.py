from django.db import models

import os, uuid, mimetypes

from django.core.urlresolvers import reverse
import simplejson as json
from PIL import Image
import requests

from djmoney.models.fields import MoneyField

from django.contrib.postgres.fields import JSONField


# --------------------------------------------------
# Abstract base classes
# --------------------------------------------------

class GenericBaseClass(models.Model):
    """
    The standard abstract base class for primary classes provides basic fields and infrastructure for
    all Model classes in this project
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime_updated = models.DateTimeField(auto_now=True, null=True, blank=True, db_index = True, help_text='The datetime this actual object was updated.', )
    datetime_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, db_index = True, help_text='The datetime this actual object was created.', )


    class Meta:
        abstract = True
        get_latest_by = '-datetime_updated'


class DescriptiveBaseClass(models.Model):
    """
    A descriptive abstract base class for primary classes provides basic descriptive fields, 
    a la Dublin Core, for concrete classes to use as a mixin.
    """
    title = models.CharField(null=True, blank=True, db_index=True, max_length=256, )
    kind = models.CharField(null=True, blank=True, db_index=True, max_length=64, )
    description = models.TextField(null=True, blank=True, )

    class Meta:
        abstract = True


class InternetResourceClass(models.Model):
    """
    A descriptive abstract base class for primary classes provides basic descriptive fields, 
    a la Dublin Core, for concrete classes to use as a mixin.
    """
    source_url = models.TextField(null=True, blank=True, )
    json = JSONField(null=True, blank=True, )

    class Meta:
        abstract = True


# --------------------------------------------------
# Margins classes
# --------------------------------------------------

class Document(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass):
    """
    Represents a unique vehicle manufacturer.
    """
    def __str__(self):
        if self.title:
            return self.title
        else:
            return 'unnamed document'

    def get_absolute_url(self):
        return reverse('document_details', args=[str(self.pk)])



        