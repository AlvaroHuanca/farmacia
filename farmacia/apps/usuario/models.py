# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class usuario(models.Model):
	"""docstring for usuario"""
	def __init__(self, arg):
		super(usuario, self).__init__()
		self.arg = arg
		