from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    """
    This class will be our user model.
    """
    adres = models.CharField(max_length=255, null=True, blank=True)
    tel = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField()
    github = models.URLField()
    linkedin = models.URLField()
    resim = models.ImageField(upload_to='media/kullaniciresimleri/%Y/%m/%d', default='media/kullaniciresimleri/resim.png')
