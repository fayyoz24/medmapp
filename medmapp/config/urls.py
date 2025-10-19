"""
URL configuration for medmapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from decouple import config
from rest_framework.permissions import IsAdminUser

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

admin_url = config("ADMIN_URL", default="admin/")
urlpatterns = [
    path(admin_url, admin.site.urls),
    path('api/v1/', include('api.v1.urls')),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Medmapp API",
        default_version='v1',
        description="Medmapp backend API documentation",
        contact=openapi.Contact(email="fayyozusmon@gmail.com"),
    ),
    public=True,
    permission_classes=(IsAdminUser,),  # Only admins can view docs
)

# Swagger for admins only
urlpatterns += [
    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-docs'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)