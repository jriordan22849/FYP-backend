# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepages', '0004_auto_20170130_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionLabel', models.CharField(max_length=250)),
            ],
        ),
    ]
