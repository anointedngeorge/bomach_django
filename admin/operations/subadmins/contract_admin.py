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




@admin.register(OperationContract)
class OperationsContractAdmin(admin.ModelAdmin):

    list_display = ['contract_title','contract_dependency','start_date','expected_end_date','contract_site',
          'contract_type','contract_value','priority',]
    exclude = ['code']

    fieldsets = (
      ('Contract', {
          'fields': ('contract_title','contract_dependency','start_date','expected_end_date','contract_site',
          'contract_type','contract_value','priority',)
      }),
      
      ('Contractor', {
          'fields': ('fullname','contractor_phone','alternative_address','country','city',
          'state','status',
          )
      }),
   )
    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generator()
        obj.save()
        return super().response_add(request, obj, post_url_continue)



