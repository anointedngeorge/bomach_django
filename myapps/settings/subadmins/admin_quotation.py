from django.contrib import admin
from django.http import HttpResponse
# Register your models here.

from settings.submodels.model_gallery import *
from settings.submodels.model_service import *
from settings.submodels.quotation_model import *



@admin.register(Quotation)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ['unit_price','qty','amount']
    exclude = ['code','amount']

    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        obj.code =  f"{uuid.uuid4().hex}"
        summ =  obj.unit_price * obj.qty
        obj.amount = summ
        obj.save()
        return super().response_add(request, obj, post_url_continue)



@admin.register(LaborBillQuotation)
class LaborBillQuotationAdmin(admin.ModelAdmin):
    exclude = ['code']

    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        obj.code =  f"{uuid.uuid4().hex}"
        obj.save()
        return super().response_add(request, obj, post_url_continue)

    class Media:
        js = (
            'custom/jquery-3.6.4.min.js', 
            'custom/app.js',       # project static folder
          
        )