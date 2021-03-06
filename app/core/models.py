import os, uuid

from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.utils.dateparse import parse_datetime
from django.utils.timezone import is_aware, make_aware
from PIL import Image
from core.utils.pdf import PDF

from haystack.utils.geo import Point

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
    name = models.CharField(null=True, blank=True, db_index=True, max_length=256, )
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

    original = models.FileField(upload_to='legistar', null=True, blank=True, max_length=1024, )
    md5 = models.CharField(null=True, blank=True, db_index=True, max_length=64, )
    meeting = models.ForeignKey('Meeting', related_name='documents', null=True, blank=True, )
    agenda_item = models.ForeignKey('AgendaItem', related_name='attachments', null=True, blank=True, )

    text = models.TextField(null=True, blank=True, )

    def __str__(self):
        if self.original:
            return '/'.join(self.original.url.split('/')[-2:])
        else:
            return 'unnamed document'

    def get_absolute_url(self):
        return reverse('document_details', args=[str(self.pk)])


@receiver(pre_save, sender=Document)
def document_text(sender, instance, *args, **kwargs):
    """
    Creates a Metadata instance whenever an Asset is added, and
    then extracts the metadata and populates the Metadata instance
    """
    if instance.original and not instance.text and instance.original.path.endswith('.pdf'):
        print('Extracting text from {}...'.format(instance.pk))
        pdf = PDF(instance.original.path)
        if pdf:
            instance.text = pdf.text
    else:
        print('Skipping extraction from {}...'.format(instance.pk))


class Meeting(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass):
    """
    Represents a unique meeting instance.
    """

    body = models.ForeignKey('Body', related_name='meetings', )
    guid = models.CharField(max_length=64, db_index=True, )

    location = models.TextField(null=True, blank=True, )
    coordinates = models.PointField(null=True, blank=True,)
    time = models.DateTimeField(null=True, blank=True, db_index = True, )

    def __str__(self):
        if self.name:
            return '{}, {}'.format(self.name, self.time)
        else:
            return 'meeting: {}'.format(self.guid)

    def get_absolute_url(self):
        return reverse('meeting_details', args=[str(self.pk)])


class Body(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass):
    """
    Represents a unique vehicle manufacturer.
    """

    slug = models.CharField(max_length=1024, db_index=True, unique=True, )

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.slug

    def get_absolute_url(self):
        return reverse('body_details', args=[str(self.pk)])


class AgendaItem(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass):
    """
    Represents a unique vehicle manufacturer.
    """

    name = models.CharField(max_length=256, db_index=True, )
    description = models.TextField(null=True, blank=True, )
    number = models.IntegerField(db_index=True, null=True, blank=True, )
    version = models.IntegerField(db_index=True, )
    meeting = models.ForeignKey('Meeting', related_name='agenda_items', null=True, blank=True, )
    type = models.CharField(max_length=256, db_index=True, null=True, blank=True, )

    def __str__(self):
        return '{}: {}'.format(self.number, self.name)

    def get_absolute_url(self):
        return reverse('agendaitem_details', args=[str(self.pk)])



@receiver(pre_save, sender=Meeting)
def meeting_location(sender, instance, *args, **kwargs):
    """
    Creates a Metadata instance whenever an Asset is added, and
    then extracts the metadata and populates the Metadata instance
    """
    if instance.json and ('coordinates' in instance.json) and (not instance.coordinates):
        print('saving coordinates...')
        lat = instance.json['coordinates']['latitude']
        lon = instance.json['coordinates']['longitude']
        instance.coordinates = 'POINT({} {})'.format(lon, lat)

    if instance.json and ('coordinates' in instance.json) and (not instance.location):
        print('saving location...')
        instance.location = instance.json['coordinates']['address']



@receiver(post_save, sender=Meeting)
def meeting_json(sender, instance, created, **kwargs):
    """
    Creates a Metadata instance whenever an Asset is added, and
    then extracts the metadata and populates the Metadata instance
    """
    if created and instance.json:
        print('new meeting, json processing')
        instance.name = instance.json['name']

        parsed_datetime = parse_datetime(instance.json['datetime'])
        if not is_aware(parsed_datetime):
            parsed_datetime = make_aware(parsed_datetime)
        instance.time = parsed_datetime

        instance.source_url = instance.json['link']

        instance.save()
        