# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264,unique=True)
# Create your models here.
