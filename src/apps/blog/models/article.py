from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "blog"
        ordering = ['-created']
