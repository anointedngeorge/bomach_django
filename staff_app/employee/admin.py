from django.contrib import admin
from employee.models import *
# Register your models here.


@admin.register(Employee)
class employeeAdmin(admin.ModelAdmin):
    list_display = ['user']