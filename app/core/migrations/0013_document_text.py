# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20161116_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
