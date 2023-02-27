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




@admin.register(OperationSite)
class OperationSiteAdmin(admin.ModelAdmin):
   
    list_display = ['site_name','date_creation','service_category','site_client']
    exclude = ['code']

    fieldsets = (
      ('Site Details', {
          'fields': ('site_name','date_creation','service_category','status','site_client','site_country',
          'site_lga',)
      }),
      
      ('Other', {
          'fields': ('site_state','site_map_location','scope_of_work','project',)
      }),
      
   )
    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generator()
        obj.save()
        return super().response_add(request, obj, post_url_continue)



