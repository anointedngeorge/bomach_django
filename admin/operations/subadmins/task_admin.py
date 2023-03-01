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
    exclude =['code','is_done']

    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generator()
        obj.save()
        return super().response_add(request, obj, post_url_continue)
    # list_display = ['user','branch','phone_number','gender','marital_status','designation','action']
    # exclude = ['user']

#     fieldsets = (
#       ('Personal', {
#           'fields': ('address','phone_number','gender','marital_status','dob','status',)
#       }),
      
#       ('Others', {
#           'fields': ('skills','designation','employment_type','salary','department')
#       }),
      
#       ('Location', {
#           'fields': ('branch','country','state','local_government','town',)
#       }),
      
#       ('Description', {
#           'fields': ('about',)
#       }),
#    )




