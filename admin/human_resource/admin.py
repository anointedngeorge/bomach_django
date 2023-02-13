from django.contrib import admin
from human_resource.models import *
# Register your models here.

@admin.register(Employee)
class HrEmployeeAdmin(admin.ModelAdmin):
    list_display = ['user','phone_number','gender','marital_status','designation','title','action']
    exclude = ['user']

    fieldsets = (
      ('Personal Information', {
          'fields': ('address','phone_number','gender','marital_status',)
      }),
      
      ('Employment History', {
          'fields': ('designation','title','employment_type','department')
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


@admin.register(EmployeeType)
class HrEmployeeTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Designation)
class HrEmployeeDesignationAdmin(admin.ModelAdmin):
    pass



@admin.register(Skill)
class HrSkillAdmin(admin.ModelAdmin):
    list_display = ['name','employee','department','created_at']

    def has_add_permission(self, request) -> bool:
        return False

@admin.register(Jobs)
class HrJobsAdmin(admin.ModelAdmin):
    list_display = ['job_title','min_salary','max_salary']

@admin.register(Job_history)
class HrJobsHistoryAdmin(admin.ModelAdmin):
    list_display = ['jobs','employee','department','start_date','end_date']

    def has_add_permission(self, request) -> bool:
        return False


@admin.register(Salary)
class HrSalaryAdmin(admin.ModelAdmin):
    list_display = ['employee','amount','reduction','paid_date','created_at']

    def has_add_permission(self, request) -> bool:
        return False


@admin.register(Department)
class HrDepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','description']


@admin.register(Advert)
class HrAdvertAdmin(admin.ModelAdmin):
    list_display = ['author','name','department','job_position','start_date','end_date','is_still_open']