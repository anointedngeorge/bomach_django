from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Register your models here.
# from fpdf import FPDF
from plugins.pdf import convert_to_file_to_pdf

from reports.models import *

import uuid
from plugins.generator import generator





@admin.register(LandSurveyReport)
class OperationsSurveyReportAdmin(admin.ModelAdmin):
    exclude = ['author','report_type','modelname','modelid']
    # list_display = ['task_title','status','due_date','task_start_date']
