from django.contrib import admin
from human_resource.models import *
# Register your models here.

@admin.register(Employee)
class HrEmployeeAdmin(admin.ModelAdmin):
    list_display = ['user','phone_number','gender','marital_status','designation','title','action']
    exclude = ['user']

#     fieldsets = (
#       ('Personal Information', {
#           'fields': ('address','phone_number','gender','marital_status',)
#       }),
      
#       ('Employment History', {
#           'fields': ('designation_id','title','employment_type','department')
#       }),
      
#       ('Location History', {
#           'fields': ('country','state','local_government','town',)
#       }),
      
#       ('Short Description', {
#           'fields': ('about',)
#       }),
#    )

    def has_add_permission(self, request) -> bool:
        return False

@admin.register(EmployeeType)
class HrEmployeeTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class HrSkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Jobs)
class HrJobsAdmin(admin.ModelAdmin):
    pass

@admin.register(Job_history)
class HrJobsHistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Salary)
class HrSalaryAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class HrDepartmentAdmin(admin.ModelAdmin):
    pass

