# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class distribuidor(models.Model):
	"""docstring for distribuidor"""
	def __init__(self, arg):
		super(distribuidor, self).__init__()
		self.arg = arg
		