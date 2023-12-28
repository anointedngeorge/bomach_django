from django.contrib import admin

# Register your models here.

from system_settings.models.model_gallery import *
from system_settings.models.model_service import *
from plugins.calculator import *


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_to','is_child_to']


@admin.register(ServiceCalculator)
class ServiceCalculatorAdmin(admin.ModelAdmin):
    list_display = ['service','up','ebb','efb','nb','nf','mncb','mncf','total']
    exclude = ['total']

    def save_model(self, request, obj, form=None, change=None) -> None:
        if obj.function != None:
            data = {
                'up':obj.up,'ebb':obj.ebb, 'efb':obj.efb,'nb':obj.nb,'nf':obj.nf,
                'mncb':obj.mncb, 'mncf':obj.mncf,'ns':obj.ns,'mncs':obj.mncs,'esrup':obj.esrup
            }
            func = {
                'function1':function1(data),
                'general_engine_calc':general_engine_calc(data)
            }
            result = func.get(obj.function)
            obj.total = result
        
        return super().save_model(request, obj, form, change)