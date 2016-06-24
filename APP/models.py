from __future__ import unicode_literals

from django.db import models

# Create your models here.
class IPdb(models.Model):
	ip = models.GenericIPAddressField()
	addr = models.CharField(max_length=64)
	date = models.DateTimeField(auto_now_add=True)