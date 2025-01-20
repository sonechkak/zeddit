from rest_framework import generics, permissions

from blog.models import Article
from blog.serializers.serializers import ArticleSerializer


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Сохранение статьи с указанием пользователя"""
        serializer.save(poster=self.request.user)
