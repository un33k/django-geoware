# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 20:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoware', '0002_auto_20170111_1831'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ocean',
            unique_together=set([('name',)]),
        ),
    ]
