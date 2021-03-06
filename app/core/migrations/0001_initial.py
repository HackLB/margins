# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 18:09
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('datetime_updated', models.DateTimeField(auto_now=True, db_index=True, help_text='The datetime this actual object was updated.', null=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The datetime this actual object was created.', null=True)),
                ('title', models.CharField(blank=True, db_index=True, max_length=256, null=True)),
                ('kind', models.CharField(blank=True, db_index=True, max_length=64, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('source_url', models.TextField(blank=True, null=True)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'get_latest_by': '-datetime_updated',
                'abstract': False,
            },
        ),
    ]
