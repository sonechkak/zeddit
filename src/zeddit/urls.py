from django.urls import path

from src.apps.blog import admin

urlpatterns = [
    path("admin/", admin.site.urls),
]
