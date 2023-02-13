from django.contrib import admin
from employee.models import *
# Register your models here.


@admin.register(Employee)
class employeeAdmin(admin.ModelAdmin):
    list_display = ['user']
    exclude = ['user']

    fieldsets = (
      ('Personal Information', {
          'fields': ('address','phone_number','gender','marital_status',)
      }),
      
      ('Employment History', {
          'fields': ('designation','title','employment_type','department','skills','salary',)
      }),
      
      ('Location History', {
          'fields': ('country','state','local_government','town',)
      }),
      
      ('Short Description', {
          'fields': ('about',)
      }),
   )

    def has_add_permission(self, request) -> bool:
        return False