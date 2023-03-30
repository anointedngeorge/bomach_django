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


PAGE_NAME = 'client_profile.html'

def currentDateTime():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d-%m-%Y_%H:%M:%S")
    return dt_string


def exportDataCsv(modeladmin, request, queryset):
    context = {}
    file_format = 'csv'
    app_name = f"{modeladmin.model.__name__}_{currentDateTime()}".lower()
    modeldata = modeladmin.printable_list if modeladmin.printable_list != None else []
    if not len(queryset) > 1:
        seed =  serializers.serialize('python', queryset)
        selected_seed =  seed[0].get('fields')
        for x in modeldata:
            if selected_seed.get(x) != None:
                context[x] = selected_seed.get(x)
            else:
                context[x] = 'empty'

        filename = os.path.realpath(f"templates/data.{file_format}")
        if os.path.exists(filename):
            open_file = open(filename).read()
            # convert to pandas dataframe
            cpd = pd.DataFrame([context])
            cpd.to_csv(filename, index=False, header=True)
            response = HttpResponse(open_file, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="{}.{}"'.format(app_name,file_format)
            return response
        else:
            return HttpResponse('File does not exist')
       
    else:
        return HttpResponse('Error: Multiple row selected. Solution: Select One Data Row.')
exportDataCsv.short_description = "Export Data in CSV"


def viewDataInPDF(modeladmin, request, queryset):
    try:
        app_name = f"{modeladmin.model.__name__}_{currentDateTime()}".lower()
        context = {}
        file_format = str('pdf').lower()
        filename = os.path.realpath(f"templates/templateResponse/client_profile_pdf.html")
        if len(queryset) ==  1:
            context = dict(modeladmin.admin_site.each_context(request),)
            data =  queryset[0]
            context['queryset']=data
            context['title'] = f"{data.get_client_fullname()}"
        # self.fileFormat(request, file_format, code)
            if os.path.exists(filename):
                template = get_template(filename)
                html  = template.render(context)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
                if not pdf.err:
                    response = HttpResponse(result.getvalue(), content_type='application/{}'.format(file_format))
                    # response['Content-Disposition'] = 'attachment; filename="{}.{}"'.format(app_name,file_format)
                    result.seek(0)
                    return response
                return None
    except Exception as e:
        return HttpResponse(e)

viewDataInPDF.short_description = "View Data PDF"


def DownloadPDF(modeladmin, request, queryset):
    try:
            app_name = f"{modeladmin.model.__name__}_{currentDateTime()}".lower()
            context = {}
            file_format = str('pdf').lower()
            filename = os.path.realpath(f"templates/templateResponse/{PAGE_NAME}")
            if len(queryset) ==  1:
                context = dict(modeladmin.admin_site.each_context(request),)
                data =  queryset[0]
                context['queryset']=data
                context['title'] = f"{data.get_client_fullname()}"
            # self.fileFormat(request, file_format, code)
                if os.path.exists(filename):
                    template = get_template(filename)
                    html  = template.render(context)
                    result = BytesIO()
                    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
                    if not pdf.err:
                        response = HttpResponse(result.getvalue(), content_type='application/{}'.format(file_format))
                        response['Content-Disposition'] = 'attachment; filename="{}.{}"'.format(app_name,file_format)
                        result.seek(0)
                        return response
                    return None
    except Exception as e:
        return HttpResponse(e)

DownloadPDF.short_description = "Download In PDF"




def ViewProfileAction(modeladmin, request, queryset):
    try:
        if len(queryset) ==  1:
            filename = os.path.realpath(f"templates/templateResponse/{PAGE_NAME}")
            context = dict(modeladmin.admin_site.each_context(request),)
            data =  queryset[0]
            context['queryset']=data
            context['title'] = f"{data.get_client_fullname()}"
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

ViewProfileAction.short_description = "View Profile"