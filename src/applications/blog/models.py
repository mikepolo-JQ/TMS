from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.TextField(null=True, blank=True, unique=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    nr_like = models.IntegerField(default=0)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_at"]
