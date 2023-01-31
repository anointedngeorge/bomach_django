
from django.urls import re_path as url
from django.views.static import serve
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from admin.api_url import api

# api versions 
VERSION = 'v1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"", include('frontend.urls')),
    path(f"", include('realestate.urls')),


    path(f"api/{VERSION}/", api.urls),
    url(r'^media/(?P<path>.*)$', serve,  {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
