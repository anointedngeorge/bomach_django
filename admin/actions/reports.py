from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.core import serializers
import pandas as pd
import os
import datetime as dt
from datetime import datetime

from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.utils.html import format_html, html_safe
from django.utils.safestring import mark_safe
from django.urls import path
from django.urls import reverse
from django.conf import settings 
from django.contrib import messages
from operations.forms import *


def currentDateTime():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d-%m-%Y_%H:%M:%S")
    return dt_string



def engineeringReportAction(modeladmin, request, queryset):
    try:
        if len(queryset) ==  1:
            filename = os.path.realpath(f"templates/templateResponse/engineering_report.html")
            context = dict(modeladmin.admin_site.each_context(request),)
            data =  queryset[0]
            context['queryset']=data
            context['title'] = f"Engineering-Report"
            context['form'] = EngineeringReportForm()
            # print(context)
                # self.fileFormat(request, file_format, code)
            if os.path.exists(filename):
                return TemplateResponse(request=request, template=filename, context=context)
            else:
                return HttpResponse('File path not found')
        else:
            return HttpResponse('Multiple Selection not allowed. You can only select one data at a time.')
    except Exception as e:
        return HttpResponse(e)

engineeringReportAction.short_description = "Engineering Report"