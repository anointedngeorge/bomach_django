from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse,JsonResponse
from django.template.response import TemplateResponse
# Register your models here.
# from fpdf import FPDF
from plugins.pdf import convert_to_file_to_pdf
from reports.models import *
from django.urls import path, include


import uuid
from plugins.code_generator import generateUniqueId
from actions.reports import ViewGeneralReportAction

# 
from system_functions.engineering_function import *

@admin.register(GeneralReport)
class OperationsContractReportAdmin(admin.ModelAdmin):
    list_display = LIST_GENERAL_REPORT
    actions = [ViewGeneralReportAction]
    exclude = ['user','status','code','author','report_type','modelname','modelid']
    
    def get_urls(self):
        qs = super().get_urls()    
        urlpatterns = [
            path('update-status/<int:id>/<str:status>/<str:function>',self.updateStatus, name='update-status')
        ]
        return urlpatterns + qs

    def updateStatus(self,request, id=None, status=None, function=''):
        message = ''
        md = self.model
        if function in globals():
            glob = globals()
            # this will check if the function with the name saved in the function parameter
            # if it is true, then, the function can be runned with the name
            fn = glob.get(function)(model=md, data={'status':status}, filter_data={'id':id}, request=request)
            if fn:
                message = "Successful"
            else:
                message = "Failed"
        else:
            message = f"{function} name does not exist! create one it."
        return JsonResponse({'message':message})

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        return self.model.objects.all().filter(user_id=request.user.id)


    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        obj.code =  generateUniqueId(8)
        obj.user_id = request.user.id
        obj.save()
        return super().response_add(request, obj, post_url_continue)
