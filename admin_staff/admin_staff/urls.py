
from django.urls import re_path as url
from django.views.static import serve
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from admin_staff.api_url import api
from django.conf import settings
# api versions 
VERSION = 'v1'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("dashboard.urls")),
    # path(f"", include('frontend.urls')),
    path(f"", include('realestate.urls')),
    path(f"", include('notifier.urls')),
    path(f"", include('human_resource.urls')),
    path(f"api/{VERSION}/", api.urls),

    url(r'^media/(?P<path>.*)$', serve,  {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
