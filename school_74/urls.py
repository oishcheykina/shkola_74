"""
URL configuration for school_74 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('vippanel/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# Используем i18n_patterns для добавления поддержки языков в URL
urlpatterns += i18n_patterns(
    path('', include('app.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
)

urlpatterns += [
    re_path(r'^robots\.txt$', serve, {'document_root': '', 'path': 'robots.txt'}),
]

if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)