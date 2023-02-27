from django.contrib import admin
from django.urls import path, reverse
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from django.contrib import messages as messag
from django.shortcuts import redirect
from django.conf import settings

# Register your models here.

from settings.submodels.model_gallery import *



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['model_name','model_id','name','url']

    def get_urls(self):
        urls = super().get_urls()
        # path('sell-plot', for urls with queries ?id=2
        new_url = [
            path('fileuploader/<str:code>/', self.admin_site.admin_view(
                self.fileUploader), name="fileuploader"),
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

