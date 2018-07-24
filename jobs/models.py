# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Job(models.Model):
	name = models.CharField(max_length=255)
	branch = models.CharField(max_length=255)
	written_tests = models.BooleanField(default=False)
	on_uat = models.BooleanField(default=False, verbose_name='On UAT')
	uat_passed = models.BooleanField(default=False, verbose_name='UAT passed')
	jenkins_passed_branch = models.BooleanField(default=False)
	merged_with_master = models.BooleanField(default=False)
	jenkins_passed_merged = models.BooleanField(default=False)
	notes = models.TextField(null=True, blank=True)
	deployment_date = models.DateTimeField(null=True, blank=True)
	done = models.BooleanField(default=False)
	repo = models.ManyToManyField('Repo')


class TestRecord(models.Model):
	TEST_LOCATIONS = [
			(1,'local'),
			(2,'UAT'),
			(3,'Jenkins'),
		]
	
	job = models.ForeignKey('Job')
	where = models.SmallIntegerField(choices=TEST_LOCATIONS, default=3)
	test_path = models.CharField(null=True, blank=True, max_length=355)
	notes = models.TextField(null=True, blank=True)

	@property
	def command(self):
		if not self.test_path:
			return ''
		command_path_split = self.test_path.split('.')
		command_path_1 = ".".join(command_path_split[:-2])
		command_path_2 = ".".join(command_path_split[-2:])
		if command_path_1 and command_path_2:
			return "bin/django-admin.py test {}:{} -sx --settings=bos2.test_pg" \
							.format(command_path_1, command_path_2)
		return ''
	


class Repo(models.Model):
	name = models.CharField(max_length=10)

	def __unicode__(self):
		return self.name