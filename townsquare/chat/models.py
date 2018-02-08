from __future__ import unicode_literals

from django.db import models


class Message(models.Model):
    when = models.DateTimeField(auto_now=True)
    content = models.TextField()
