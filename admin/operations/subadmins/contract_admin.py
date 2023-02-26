from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Register your models here.
# from fpdf import FPDF
from plugins.pdf import convert_to_file_to_pdf

from operations.models import *

@admin.register(OperationContract)
class OperationsContractAdmin(admin.ModelAdmin):

    list_display = ['contract_title','start_date','expected_end_date','project','site',
          'project_type','project_value']
    # exclude = ['user']

    fieldsets = (
      ('Contract', {
          'fields': ('contract_title','start_date','expected_end_date','project','site',
          'project_type','project_value',)
      }),
      
      ('Contractor', {
          'fields': ('fullname','contractor_phone','alternative_address','country','city',
          'state','status',
          )
      }),
   )




