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
        article = Article.objects.filter(pk=kwargs["pk"], poster=request.user)
        if article.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError("Вы не можете удалять статью. Вы не являетесь ее автором.")
