from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
# Register your models here.
# from fpdf import FPDF
from human_resource.subadmins.admin_employee import *


@admin.register(Salary)
class HrSalaryAdmin(admin.ModelAdmin):
    list_display = ['employee','amount','reduction','paid_date','created_at']

    def has_add_permission(self, request) -> bool:
        return False