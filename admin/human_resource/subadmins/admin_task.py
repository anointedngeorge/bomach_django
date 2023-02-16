from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
# Register your models here.
# from fpdf import FPDF



@admin.register(Task)
class HrTaskAdmin(admin.ModelAdmin):
    list_display = ['author','name','start_date','end_date']


    