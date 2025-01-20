from django.urls import path, include

from ..blog.urls import urlpatterns as blog_api_urls

app_name = "api"

urlpatterns = [
    path("v1/", include((blog_api_urls, "blog"), namespace="blog")),
]
