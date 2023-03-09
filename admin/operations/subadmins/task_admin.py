from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Register your models here.
# from fpdf import FPDF
from plugins.pdf import convert_to_file_to_pdf
from operations.models import *
import uuid
from plugins.generator import generator


@admin.register(OperationTask)
class OperationsTaskAdmin(admin.ModelAdmin):
    # list_display = []
    exclude =['user','code','is_done']
    list_display = ['user','task_category','task_title','task_project','action']
   

    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generator()
        obj.user = request.user
        obj.save()
        return super().response_add(request, obj, post_url_continue)
    




