# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20161111_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='original',
            field=models.FileField(blank=True, max_length=1024, null=True, upload_to='legistar'),
        ),
    ]
