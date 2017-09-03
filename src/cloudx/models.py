# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Data(models.Model) :
	name = models.CharField(max_length=100)
	managerid = models.IntegerField(null=True, blank=True)

	# for the unicode string 
	def __unicode__(self) :
		return self.name

