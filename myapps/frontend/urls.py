
from django.contrib import admin
from django.urls import path, include
from frontend.views import index


app_name = 'frontend'
urlpatterns = [
    path('', index, name='index'),
    path('<str:pagename>/<str:page_title>', index, name='index'),
]

