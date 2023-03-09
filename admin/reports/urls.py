
from django.urls import re_path as url
from django.views.static import serve
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import reports.views as view
# api versions 
VERSION = 'v1'
# template_name, model
urlpatterns = [
    path(f"get-report/<str:template_name>/<str:model>/", view.getReport, name='get-report'),

]