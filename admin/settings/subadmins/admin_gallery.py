from django.contrib import admin

# Register your models here.

from settings.submodels.model_gallery import *



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['model_name','model_id','name','url']

