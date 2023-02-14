from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
# Register your models here.
# from fpdf import FPDF
from human_resource.subadmins.admin_employee import *



@admin.register(Advert)
class HrAdvertAdmin(admin.ModelAdmin):
    list_display = ['author','name','department','job_position','start_date','end_date',
    'is_still_open']


    