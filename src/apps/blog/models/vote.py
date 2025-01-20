from django.contrib.auth.models import models, User

from ..models.article import Article


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
