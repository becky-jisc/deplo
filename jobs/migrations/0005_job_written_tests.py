# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20180628_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='written_tests',
            field=models.BooleanField(default=False),
        ),
    ]