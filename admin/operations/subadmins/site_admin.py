from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Register your models here.
# from fpdf import FPDF
from plugins.pdf import convert_to_file_to_pdf

from operations.models import *

@admin.register(OperationSite)
class OperationSiteAdmin(admin.ModelAdmin):
    """
    site_country = CountryField(blank_label="(select country)", default='---',max_length=250)
    site_lga = models.CharField(max_length=200, null=True)
    site_state = models.CharField(max_length=200, null=True)
    site_map_location = models.CharField(max_length = 150, null=True)
    scope_of_work = models.CharField(max_length = 150, null=True)
    project = models.ForeignKey(OperationProject, on_delete=models.CASCADE, 
    related_name='project_site_related')
    created_at = models.DateField(auto_now=True)
    
    """
    list_display = ['site_name','date_creation','service_category','site_client']
    # exclude = ['user']

    fieldsets = (
      ('Site Details', {
          'fields': ('site_name','date_creation','service_category','status','site_client','site_country',
          'site_lga',)
      }),
      
      ('Other', {
          'fields': ('site_state','site_map_location','scope_of_work','project',)
      }),
      
   )




