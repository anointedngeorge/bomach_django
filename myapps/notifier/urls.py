
from django.contrib import admin
from django.urls import path, include
from notifier.views import *



urlpatterns = [
    path('notifier/', index),
]
