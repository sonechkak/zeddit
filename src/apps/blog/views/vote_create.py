from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from ..models import Article, Vote
from ..serializers.serializers import VoteSerializer


class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Получение голоса с указанием пользователя и статьи"""
        user = self.request.user
        article = Article.objects.get(pk=self.kwargs["pk"])
        return Vote.objects.filter(voter=user, article_id=article)

    def perform_create(self, serializer):
        """Создание голоса"""
        if self.get_queryset().exists():
            raise ValidationError("Вы уже проголосовали за эту статью")

        user = self.request.user
        article = Article.objects.get(pk=self.kwargs["pk"])
        serializer.save(voter=user, article=article)

    def delete(self, request, *args, **kwargs):
        """Удаление голоса"""
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT, data={"detail": "Голос успешно удален"})
        else:
            raise ValidationError("Вы еще не голосовали за эту статью")
