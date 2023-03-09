from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
# Register your models here.
# from fpdf import FPDF
from human_resource.subadmins.admin_employee import *
import uuid
from plugins.generator import generator


@admin.register(Designation)
class HrEmployeeDesignationAdmin(admin.ModelAdmin):
    list_display = ['roles','name']
    exclude = ['code']

    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generator()
        obj.save()
        return super().response_add(request, obj, post_url_continue)
