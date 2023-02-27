from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
# Register your models here.
# from fpdf import FPDF
import uuid
from plugins.generator import generator



@admin.register(Task)
class HrTaskAdmin(admin.ModelAdmin):
    list_display = ['author','name','start_date','end_date']
    exclude = ['code']

    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generator()
        obj.save()
        return super().response_add(request, obj, post_url_continue)


    