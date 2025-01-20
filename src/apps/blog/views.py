from django.shortcuts import render
from rest_framework import generics

from .models import Article


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
