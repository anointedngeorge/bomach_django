
from django.urls import re_path as url
from django.views.static import serve
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from human_resource import views

urlpatterns = [
    path(f"message/", views.message, name='message'),
]
