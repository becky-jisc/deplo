# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('where', models.SmallIntegerField(choices=[(1, 'local'), (2, 'UAT'), (3, 'Jenkins')])),
                ('test_path', models.CharField(max_length=355)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='branch',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='testrecord',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job'),
        ),
    ]
