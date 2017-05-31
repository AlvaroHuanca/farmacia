# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class crear_compra(models.Model):
	"""docstring for crear_compra"""
	def __init__(self, arg):
		super(crear_compra, self).__init__()
		self.arg = arg
		