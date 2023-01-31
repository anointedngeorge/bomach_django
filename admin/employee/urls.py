
from django.contrib import admin
from django.urls import path, include
from frontend.views import index


app_name = "employee"

urlpatterns = [
    path('/employee/', index),
]
