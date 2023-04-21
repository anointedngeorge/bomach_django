from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Register your models here.
# from fpdf import FPDF
from plugins.pdf import convert_to_file_to_pdf
from actions.generator import codeGenerator
from actions.reports import ViewEngineeringReportAction
from reports.models import *

import uuid
from plugins.generator import generator

@admin.register(EngineeringReport)
class OperationsEngineeringReportAdmin(admin.ModelAdmin):
    exclude = ['author','report_type','modelname','modelid','code','status']
    list_display = Engineering_ADMIN_LIST
    actions = [ViewEngineeringReportAction,codeGenerator]

    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        obj.code =  f"{uuid.uuid4().hex}"
        obj.save()
        return super().response_add(request, obj, post_url_continue)