from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse,JsonResponse
from django.template.response import TemplateResponse
# Register your models here.
# from fpdf import FPDF
from plugins.pdf import convert_to_file_to_pdf
from actions.generator import codeGenerator
from actions.reports import ViewEngineeringReportAction
from reports.models import *
from django.urls import path, include
import uuid
from plugins.generator import generator
from system_functions.engineering_function import *

@admin.register(EngineeringReport)
class OperationsEngineeringReportAdmin(admin.ModelAdmin):
    exclude = ['author','report_type','modelname','modelid','code','status']
    list_display = Engineering_ADMIN_LIST
    actions = [ViewEngineeringReportAction,codeGenerator]

    # engineering-status
    def get_urls(self):
        qs = super().get_urls()    
        urlpatterns = [
            path('engineering-status/<int:id>/<str:status>/<str:function>',self.engineeringStatus, name='engineering-status')
        ]
        return urlpatterns + qs

    def engineeringStatus(self,request, id=None, status=None, function=''):
        message = ''
        md = self.model
        if function in globals():
            glob = globals()
            # this will check if the function with the name saved in the function parameter
            # if it is true, then, the function can be runned with the name
            fn = glob.get(function)(model=md, data={'status':status, 'user_id':request.user.id}, filter_data={'id':id}, request=request)
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
        obj.code =  f"{uuid.uuid4().hex}"
        obj.user_id = request.id
        obj.save()
        return super().response_add(request, obj, post_url_continue)