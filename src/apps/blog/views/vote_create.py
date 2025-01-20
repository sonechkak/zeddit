from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

from ..models import Article, Vote
from ..serializers.serializers import VoteSerializer


class VoteCreate(generics.CreateAPIView):
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
