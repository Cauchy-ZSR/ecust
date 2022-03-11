"""ecustCircle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="师生圈接口文档",
        default_version="v1",
        description="接口描述",
        terms_of_service="",
        contact=openapi.Contact(email="1989004969@qq.com"),
        license=openapi.License(name="BSD LICENSE")
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^userApi/',include('user.urls')),
    re_path(r'^forumApi/',include('forum.urls')),
    re_path(r'^chatApi/',include('chat.urls')),
    re_path(r'^notifyInfoApi/',include('notify.urls')),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
