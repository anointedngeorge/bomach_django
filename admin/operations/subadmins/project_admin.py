from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Register your models here.
# from fpdf import FPDF
from plugins.pdf import convert_to_file_to_pdf
from operations.models import *
from operations.forms import ProjectForm

@admin.register(OperationProject)
class OperationProjectAdmin(admin.ModelAdmin):
    
    list_display = ['project_name','start_date','expected_end_date','client',
    'budget','hour_estimated']
    exclude = ['project_id']
    # form = ProjectForm

    fieldsets = (
      ('Projects', {
          'fields': ('project_name','project_category','department','project_members',)
      }),

     ('Project Information', {
          'fields': ('start_date','budget','hour_estimated','expected_end_date','client',)
      }),

    ('description', {
          'fields': ('project_owner','project_desciption',)
      }),
    
   )




