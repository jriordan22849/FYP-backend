# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 18:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20170130_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='surveyName',
        ),
    ]
