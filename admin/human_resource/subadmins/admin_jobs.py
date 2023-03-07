from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
# Register your models here.
# from fpdf import FPDF
from human_resource.subadmins.admin_employee import *
import uuid
from plugins.generator import generator



@admin.register(Jobs)
class HrJobsAdmin(admin.ModelAdmin):
    list_display = ['employee','description']

# @admin.register(Job_history)
class HrJobsHistoryAdmin(admin.ModelAdmin):
    list_display = ['employee','jobs','department','start_date','end_date']
    list_filter = ['employee','jobs', 'department','start_date','end_date']
    exclude = ['code',]

    def has_add_permission(self, request) -> bool:
        return False
    
    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generator()
        obj.save()
        return super().response_add(request, obj, post_url_continue)