from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
# Register your models here.
# from fpdf import FPDF
from human_resource.admin.admin_employee import *
import uuid
from plugins.code_generator import generateUniqueId


@admin.register(EmployeeType)
class HrEmployeeTypeAdmin(admin.ModelAdmin):
    exclude = ['code']

    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generateUniqueId()
        obj.save()
        return super().response_add(request, obj, post_url_continue)