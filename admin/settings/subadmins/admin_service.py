from django.contrib import admin

# Register your models here.

from settings.submodels.model_gallery import *
from settings.submodels.model_service import *



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_to','is_child_to']


@admin.register(ServiceCalculator)
class ServiceCalculatorAdmin(admin.ModelAdmin):
    list_display = ['service','up','ebb','efb','nb','mncb','mncf']