from datetime import datetime

from django.db import models


class Post(models.Model):
    title = models.TextField(null=True, blank=True, unique=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    nr_like = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]
