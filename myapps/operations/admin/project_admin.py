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
import uuid
from plugins.code_generator import generateUniqueId
from plugins.dropdown import dictDropdown


@admin.register(OperationProject)
class OperationProjectAdmin(admin.ModelAdmin):
    
    list_display = ['user','status','project_name','start_date','expected_end_date','client',
    'budget',]
    exclude = ['project_id','code']
    # form = ProjectForm

    fieldsets = (
      ('Projects', {
          'fields': ('project_name','project_category','department','project_members',)
      }),

     ('Project Information', {
          'fields': ('start_date','budget','expected_end_date','client',)
      }),

    ('description', {
          'fields': ('project_dependency','project_desciption',)
      }),
    
   )
    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generateUniqueId()
        obj.user = request.user
        obj.save()
        return super().response_add(request, obj, post_url_continue)

    




