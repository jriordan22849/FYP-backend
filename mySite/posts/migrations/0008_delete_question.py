# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_question_surveyname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
