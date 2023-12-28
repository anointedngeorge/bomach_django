from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse,HttpRequest

# Register your models here.
# from fpdf import FPDF
from human_resource.subadmins.admin_employee import *
import uuid
from plugins.generator import generator


@admin.register(Designation)
class HrEmployeeDesignationAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    exclude = ['code']


    def get_queryset(self, request: HttpRequest):
        if not request.user.is_superuser:
            qs = self.model.filter(user_id=request.user.d)
            return qs
        return super().get_queryset(request)
        

    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generator()
        obj.save()
        return super().response_add(request, obj, post_url_continue)
