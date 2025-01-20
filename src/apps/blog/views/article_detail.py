from rest_framework import generics

from ..serializers.serializers import ArticleSerializer
from ..models.article import Article


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_update(self, serializer):
        """Обновление статьи с указанием пользователя"""
        serializer.save(poster=self.request.user)

    def perform_destroy(self, instance):
        """Удаление статьи с указанием пользователя"""
        instance.delete()
