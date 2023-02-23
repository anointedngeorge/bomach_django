from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Register your models here.
# from fpdf import FPDF
from plugins.pdf import convert_to_file_to_pdf

from operations.models import *

@admin.register(OperationProject)
class OperationProjectAdmin(admin.ModelAdmin):
    
    list_display = ['project_id','project_name','start_date','expected_end_date','client',
    'budget','hour_estimated']
    # exclude = ['user']

    fieldsets = (
      ('Projects', {
          'fields': ('project_id','project_name','start_date','expected_end_date',)
      }),

     ('Extra', {
          'fields': ('project_category','client','budget','hour_estimated',)
      }),

    ('description', {
          'fields': ('project_owner','project_desciption',)
      }),
    
   )




