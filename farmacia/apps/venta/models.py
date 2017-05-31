# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class crear_venta(models.Model):
	"""docstring for crear_venta"""
	def __init__(self, arg):
		super(crear_venta, self).__init__()
		self.arg = arg