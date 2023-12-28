from typing import Any, Optional
from django.contrib import admin
from django.contrib.admin.sites import site
from django.http import request
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.template.response import TemplateResponse

from frontend.models import *
from plugins.image_resizer import imageRizer

width = 400
height = 400

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    
    def response_add(self, request: HttpRequest, obj, post_url_continue=None) -> HttpResponse:
        # resize image to 300, 300
        imageRizer(image_path=obj.image.path, width=width, height=height)
        return super().response_add(request, obj, post_url_continue)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    
    list_display = LIST_DISPLAY_SETTINGS

    def response_add(self, request: HttpRequest, obj, post_url_continue=None) -> HttpResponse:
        # resize image to 300, 300
        imageRizer(image_path=obj.logo.path, width=width, height=height)
        return super().response_add(request, obj, post_url_continue)

    def save_model(self, request, obj, form=None, change=None) -> None:
        obj.id = 1
        return super().save_model(request, obj, form, change)



@admin.register(DataJosn)
class DataJsonAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    
    def response_add(self, request: HttpRequest, obj, post_url_continue=None) -> HttpResponse:
        # resize image to 300, 300
        imageRizer(image_path=obj.image.path, width=width, height=height)
        return super().response_add(request, obj, post_url_continue)




@admin.register(NowSelling)
class NowSellingAdmin(admin.ModelAdmin):
        
    def response_add(self, request: HttpRequest, obj, post_url_continue=None) -> HttpResponse:
        # resize image to 300, 300
        imageRizer(image_path=obj.image.path, width=width, height=height)
        return super().response_add(request, obj, post_url_continue)
    
    
    def save_model(self, request, obj, form=None, change=None) -> None:
        obj.id = 1
        return super().save_model(request, obj, form, change)
    

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
        pass
    # def save_model(self, request, obj, form=None, change=None) -> None:
    #     obj.id = 1
    #     return super().save_model(request, obj, form, change)



@admin.register(About)
class AboutusAdmin(admin.ModelAdmin):

    def response_add(self, request: HttpRequest, obj, post_url_continue=None) -> HttpResponse:
        # resize image to 300, 300
        imageRizer(image_path=obj.image.path, width=width, height=height)
        return super().response_add(request, obj, post_url_continue)

    def save_model(self, request, obj, form=None, change=None) -> None:
        obj.id = 1
        return super().save_model(request, obj, form, change)