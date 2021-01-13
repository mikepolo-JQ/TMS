from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.TextField(null=True, blank=True, unique=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    who_likes = models.ManyToManyField(User, related_name="user_like", blank=True)

    nr_views = models.IntegerField(default=0)

    @property
    def nr_likes(self):
        return self.who_likes.count()

    def is_liked_by(self, user) -> bool:
        return Post.objects.filter(pk=self.pk, who_likes=user).exists()

    @property
    def all_post_pk(self):
        posts_pk = [post.pk for post in Post.objects.all()]
        return posts_pk

    class Meta:
        ordering = ["-created_at"]
