from rest_framework import generics
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Article
from blog.serializers.serializers import ArticleSerializer


class ArticleRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        article = Article.objects.filter(pk=kwargs["pk"], poster=self.request.user)
        if article.poster == self.request.user or self.request.user.is_superuser or self.request.user.is_staff:
            return self.destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied("Вы не можете удалить эту статью")
