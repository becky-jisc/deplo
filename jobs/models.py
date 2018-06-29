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
	where = models.SmallIntegerField(choices=TEST_LOCATIONS)
	test_path = models.CharField(max_length=355)
	notes = models.TextField(null=True, blank=True)


class Repo(models.Model):
	name = models.CharField(max_length=10)

	def __unicode__(self):
		return self.name