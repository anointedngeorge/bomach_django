from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Register your models here.
# from fpdf import FPDF

from plugins.pdf import convert_to_file_to_pdf
import uuid
from plugins.generator import generator
from actions.generator import codeGenerator
from actions.exportToDifferentFormat import *



@admin.register(Employee)
class HrEmployeeAdmin(admin.ModelAdmin):
    list_display = ['user','branch','phone_number','gender','marital_status','designation','action']
    printable_list = ['user']
    exclude = ['user', 'code']
    actions = [codeGenerator, ViewProfileAction]
    

    fieldsets = (
      ('Personal', {
          'fields': ('address','phone_number','gender','marital_status','dob','status',)
      }),
      
      ('Others', {
          'fields': ('skills','designation','employment_type','salary','department')
      }),
      
      ('Location', {
          'fields': ('branch','country','state','local_government','town',)
      }),

      ('Add Special Roles (If ANY?)', {
          'fields': ('special_roles',)
      }),
      
      ('Description', {
          'fields': ('about',)
      }),
   )
    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generator()
        obj.save()
        return super().response_add(request, obj, post_url_continue)

        
    def get_urls(self):
        urls = super().get_urls()
        
        new_url = [
            path('employee-profile/', self.admin_site.admin_view(self.employee_profile) , 
            name="employee-profile"),
    
            ]
        urls = new_url + urls
        return urls

    def has_add_permission(self, request) -> bool:
        return False

    def employee_profile(self, request):
        template =  "pdf/pdf_employee_profile.html"
        return convert_to_file_to_pdf(template=template)



