from rest_framework import serializers

from ..models.article import Article
from ..models.vote import Vote


class ArticleSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source="poster.username")
    poster_id = serializers.ReadOnlyField(source="poster.id")

    class Meta:
        model = Article
        fields = ["id", "title", "url", "poster", "poster_id", "created"]


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["id"]
