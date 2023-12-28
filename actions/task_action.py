from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.core import serializers
import pandas as pd
import os
import datetime as dt
from datetime import datetime

from io import BytesIO
from reports.models.reportmodel.engineering_site_report import EngineeringReport
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.utils.html import format_html, html_safe
from django.utils.safestring import mark_safe
from django.urls import path
from django.urls import reverse
from django.conf import settings 
from django.contrib import messages as flash_message
from operations.forms import *
from plugins.permissions import checkCodenameInPermGroup
from plugins.status_actions import statusActions
def currentDateTime():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d-%m-%Y_%H:%M:%S")
    return dt_string




def ViewTaskAction(modeladmin, request, queryset):
    try:
        check = checkCodenameInPermGroup(
            group_name='staff',
            permission_codename='can_access_engineering_report'
        )
        if True:
            if len(queryset) ==  1:
                filename = os.path.realpath(f"templates/templateResponse/view_task_profile.html")
                context = dict(modeladmin.admin_site.each_context(request),)
                data =  queryset[0]
                context['queryset']=data
                context['title'] = f"Task Profile for {data.get_profile()}"
                # todo: doing
    # doing: completed, redo
    # redo:suspended, completed, redo
                data2 = {
                    'pending':[
                        {'name':'Todo','url':'', 'status':'doing','classname':'btn btn-sm btn-primary'},
                    ],
                    'doing':[
                        {'name':'Accept','url':'', 'status':'completed','classname':'btn btn-sm btn-primary',
                        'function':'updateEngineeringReport'},
                        {'name':'Redo','url':'', 'status':'redo','classname':'btn btn-sm btn-warning',
                        'function':'updateEngineeringReport'},
                    ],
                    'redo':[
                            {'name':'Suspend','url':'', 'status':'suspending','classname':'btn btn-sm btn-dark',
                            'function':'updateEngineeringReport'},

                            {'name':'completed','url':'', 'status':'completed','classname':'btn btn-sm btn-success',
                            'function':'updateEngineeringReport'},
                            {'name':'Redo','url':'', 'status':'redo','classname':'btn btn-sm btn-success',
                            'function':'updateEngineeringReport'},
                        ],
                    'query':{}
                }
                context['action'] = statusActions(
                    data=data2,
                    status=data.status,
                    request=request
                )
                # print(context)
                # self.fileFormat(request, file_format, code)
                if os.path.exists(filename):
                    return TemplateResponse(request=request, template=filename, context=context)
                else:
                    return HttpResponse('File path not found')
            else:
                return HttpResponse('Multiple Selection not allowed. You can only select one data at a time.')
        else:
            flash_message.error(request, 'Permission Denied.')
    except Exception as e:
        return HttpResponse(e)

ViewTaskAction.short_description = "View Task Profile"



def TaskReportAction(modeladmin, request, queryset):
    try:
        check = checkCodenameInPermGroup(
            group_name='staff',
            permission_codename='can_access_engineering_report'
        )
        if True:
            if len(queryset) ==  1:
                filename = os.path.realpath(f"templates/templateResponse/view_task_reporting_sheet.html")
                context = dict(modeladmin.admin_site.each_context(request),)
                data =  queryset[0]
                context['queryset']=data
                context['title'] = f"Task Report: {data.get_profile()}"

                # print(context)
                # self.fileFormat(request, file_format, code)
                if os.path.exists(filename):
                    return TemplateResponse(request=request, template=filename, context=context)
                else:
                    return HttpResponse('File path not found')
            else:
                return HttpResponse('Multiple Selection not allowed. You can only select one data at a time.')
        else:
            flash_message.error(request, 'Permission Denied.')
    except Exception as e:
        return HttpResponse(e)

TaskReportAction.short_description = "Task Reporting Sheet"

