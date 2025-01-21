from rest_framework import generics, permissions

from blog.models import Article
from blog.serializers.serializers import ArticleSerializer
from rest_framework.exceptions import PermissionDenied


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.is_anonymous:
            raise PermissionDenied("Вы не авторизованы")
        serializer.save(poster=self.request.user)
