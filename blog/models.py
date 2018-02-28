from __future__ import unicode_literals

from django.db import models

# Create your models here.
from proje.settings import AUTH_USER_MODEL


class Blog(models.Model):
    """
    This class will be our blog model.
    """
    title = models.CharField(max_length=255, null=True, blank=True, help_text="Bu alani bos birakabilirsiniz.")
    author = models.ForeignKey(AUTH_USER_MODEL)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/blogresimleri/%Y/%m/%d', default='media/blogresimleri/blog.jpg')

    def __unicode__(self):
        return '{}'.format(self.title)