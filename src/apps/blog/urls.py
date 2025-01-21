from django.urls import path, include

from .views import (
    article_list,
    article_detail,
    vote_create,
    article_retrieve_destroy,
)

app_name = "blog"

urlpatterns = [
    path("articles/", article_list.ArticleListView.as_view(), name="article-list"),
    # path("articles/<int:pk>/", article_detail.ArticleDetailView.as_view(), name="article-detail"),
    path(
        "articles/<int:pk>/",
        article_retrieve_destroy.ArticleRetrieveDestroyView.as_view(),
        name="article-retrieve-destroy"
    ),
    path("articles/<int:pk>/vote/", vote_create.VoteCreate.as_view(), name="vote-create"),
]
