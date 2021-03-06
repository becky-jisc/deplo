# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('branch', models.CharField(max_length=256)),
                ('merged_with_master', models.BooleanField(default=False)),
                ('on_uat', models.BooleanField(default=False)),
                ('uat_passed', models.BooleanField(default=False)),
                ('jenkins_passed_branch', models.BooleanField(default=False)),
                ('jenkins_passed_merged', models.BooleanField(default=False)),
            ],
        ),
    ]
