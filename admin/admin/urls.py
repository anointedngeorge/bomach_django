
from django.urls import re_path as url
from django.views.static import serve
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from admin.api_url import api
from django.conf import settings
# api versions 
VERSION = 'v1'

urlpatterns = [
    path(f"{settings.ADMIN_LOGIN_PATH}", admin.site.urls),
    path(f"", include('frontend.urls')),
    path(f"", include('realestate.urls')),
    path(f"", include('notifier.urls')),
    path(f"", include('reports.urls')),
    path(f"api/{VERSION}/", api.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    
    url(r'^media/(?P<path>.*)$', serve,  {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
