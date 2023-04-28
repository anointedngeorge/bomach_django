from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse,JsonResponse
from django.template.response import TemplateResponse
# Register your models here.
# from fpdf import FPDF
from plugins.pdf import convert_to_file_to_pdf
from operations.models import *
import uuid
from plugins.generator import generator
from actions.task_action import (
    ViewTaskAction,
    TaskReportAction
)
from system_functions.engineering_function import *


@admin.register(OperationTask)
class OperationsTaskAdmin(admin.ModelAdmin):
    # list_display = []

    exclude =['user','code','is_done']
    list_display = ['branch','user','task_category','task_title','task_project','action']
    list_filter = ['branch']
    actions = [ViewTaskAction,TaskReportAction]


    def get_urls(self):
        qs = super().get_urls()    
        urlpatterns = [
            path('update-status/<int:id>/<str:status>/<str:function>',self.updateStatus, 
            name='update-status')
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
        rq = self.model.objects.all().filter(user_id=request.user.id)
        return rq
        

    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generator()
        obj.user = request.user
        obj.save()
        return super().response_add(request, obj, post_url_continue)
    




