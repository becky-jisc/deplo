# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 08:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20180629_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='deployed',
        ),
    ]
