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

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from plugins.permissions import checkCodenameInPermGroup
from django.contrib import messages as flash_message
from plugins.status_actions import statusActions



PAGE_NAME = 'appointment_profile.html'

def currentDateTime():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d-%m-%Y_%H:%M:%S")
    return dt_string




def ViewAppointmentProfile(modeladmin, request, queryset):
    try:
        group_name = request.user.roles
        checkCodenameInGroup =  checkCodenameInPermGroup(
            group_name=group_name, 
            permission_codename='can_view_appointment_details',
            
        )
        if (checkCodenameInGroup):
            if len(queryset) ==  1:
                filename = os.path.realpath(f"templates/templateResponse/{PAGE_NAME}")
                context = dict(modeladmin.admin_site.each_context(request),)
                data =  queryset[0]
                context['queryset']=data
                context['title'] = f"Appointment - {data.page_title()}".title()
                data =  {
                    'pending':[
                        {'name':'Confirm','url':'confirm/', 'classname':'btn btn-sm btn-primary'},
                        {'name':'Send Reminder','url':'confirm/', 'classname':'btn btn-sm btn-warning'},
                        {'name':'Cancel Appointment','url':'confirm/', 'classname':'btn btn-sm btn-danger'}
                    ],
                    'query':{'id':1}
                }
                context['action_btn'] = statusActions(data=data,request=request)


                    # self.fileFormat(request, file_format, code)
                if os.path.exists(filename):
                    return TemplateResponse(request=request, template=filename, context=context)
                else:
                    return HttpResponse('File path not found')
            else:
                return HttpResponse('Multiple Selection not allowed. You can only select one data at a time.')
        else:
            flash_message.error(request, "Permission denied.")
    except Exception as e:
        return HttpResponse(e)

ViewAppointmentProfile.short_description = "View Appointment"



