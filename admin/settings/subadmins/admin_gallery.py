from django.contrib import admin
from django.urls import path, reverse
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from django.contrib import messages as messag
from django.shortcuts import redirect
from django.conf import settings
# Register your models here.
from settings.submodels.model_gallery import *
import requests as req



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['model_name','model_id','name','url']

    def get_urls(self):
        urls = super().get_urls()
        # path('sell-plot', for urls with queries ?id=2
        new_url = [
            path('fileuploader/<str:code>/', self.admin_site.admin_view(
                self.fileUploader), name="fileuploader"),

            path('get-files/<str:code>/', self.admin_site.admin_view(
                self.get_files), name="get-files"),
        ]
        return new_url + urls

    
    def fileUploader(self, request, code=None):
        context = dict(self.admin_site.each_context(request),)
        dictobj =  request.GET.dict()
        context['site_title'] = 'File Uploader'
        context['title'] = 'File uploader'
        context['code'] = code
        context['model'] = dictobj.get('model')
        return TemplateResponse(request, 
        "templateResponse/setting/gallary.html", context=context)

    def get_files(self, request, code=None):
        context = dict(self.admin_site.each_context(request),)
        dictobj =  request.GET.dict()
        context['site_title'] = 'Get files'
        context['title'] = 'Get files'
        context['code'] = code
        context['model'] = dictobj.get('model')
        url = "https://bomachgroup.com/apiadmin/api/v1/media/get-gallery-image/{code}/"
        files =  req.get(url)
        result =  files.json()
        context["files"] = result
        
        return TemplateResponse(request, 
        "templateResponse/setting/files.html", context=context)

