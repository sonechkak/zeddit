from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    # API
    path("api/", include("api.urls", namespace="api")),
    # Auth
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # Docs
    # DRF Spectacular : OpenAPI 3.0
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    # ReDoc
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
