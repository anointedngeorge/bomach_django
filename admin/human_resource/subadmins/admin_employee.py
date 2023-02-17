from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse

# Register your models here.
# from fpdf import FPDF

from plugins.pdf import convert_to_file_to_pdf

@admin.register(Employee)
class HrEmployeeAdmin(admin.ModelAdmin):
    list_display = ['user','phone_number','gender','marital_status','designation','title','action']
    exclude = ['user']

    fieldsets = (
      ('Personal Information', {
          'fields': ('address','phone_number','gender','marital_status','date_of_birth','status',)
      }),
      
      ('Employment History', {
          'fields': ('skills','designation','title','employment_type','department')
      }),
      
      ('Location History', {
          'fields': ('country','state','local_government','town',)
      }),
      
      ('Short Description', {
          'fields': ('about',)
      }),
   )

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



