from django.contrib import admin

from .models import Article, Vote


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "poster", "created")
    search_fields = ("title", "poster")
    list_filter = ("created",)
    date_hierarchy = "created"


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("voter", "article")
    search_fields = ("voter", "article")
    list_filter = ("article",)