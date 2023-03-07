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

    list_display = ['branch','user','contract_title','contract_value','start_date','expected_end_date','contract_site',
          'priority','action']
    exclude = ['code']

    fieldsets = (
      ('Contract', {
          'fields': ('branch','contract_title','contract_dependency','start_date','expected_end_date','contract_site',
          'contract_type','contract_value','priority','contract_description',)
      }),
      
      ('Contractor', {
          'fields': ('fullname','contractor_phone','country','city',
          'state','alternative_address','status',
          )
      }),
   )
    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generator()
        obj.user = request.user
        obj.save()
        return super().response_add(request, obj, post_url_continue)



