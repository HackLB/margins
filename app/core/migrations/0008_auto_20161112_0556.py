# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_meeting_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='body',
            name='slug',
            field=models.CharField(db_index=True, max_length=1024, unique=True),
        ),
    ]