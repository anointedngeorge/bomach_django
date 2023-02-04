
from django.urls import re_path as url
from django.views.static import serve
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# api versions 
VERSION = 'v1'

urlpatterns = [
    path(f"{settings.ADMIN_LOGIN_PATH}", admin.site.urls),
    path(f"", include('frontend.urls')),
    
    url(r'^media/(?P<path>.*)$', serve,  {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
