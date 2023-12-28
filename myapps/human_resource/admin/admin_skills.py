from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
# Register your models here.
# from fpdf import FPDF
from human_resource.admin.admin_employee import *
import uuid
from plugins.code_generator import generateUniqueId


@admin.register(Skill)
class HrSkillAdmin(admin.ModelAdmin):
    list_display = ['name','designation','created_at']
    exclude = ['code']

    # def has_add_permission(self, request) -> bool:
    #     return False

    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generateUniqueId()
        obj.save()
        return super().response_add(request, obj, post_url_continue)