from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Register your models here.
# from fpdf import FPDF
from plugins.pdf import convert_to_file_to_pdf

from operations.models import *

import uuid
from plugins.generator import generator





@admin.register(EngineeringReport)
class OperationsEngineeringReportAdmin(admin.ModelAdmin):
    exclude = ['author','report_type','modelname','modelid']
    list_display = Engineering_ADMIN_LIST
