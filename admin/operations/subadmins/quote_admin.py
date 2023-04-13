from django.contrib import admin
from operations.models import *
from plugins.calculator import *
from plugins.generator import generator
from django.http import HttpResponse

from actions.serviceQuote import *


@admin.register(QuotesModel)
class QuotesModelAdmin(admin.ModelAdmin):
    list_display = ['code','customer','services','nb','nf','ns','total','status','action']
    exclude = ['total','code','amount_deposited','amount_pending']
    actions = [ViewProfileAction]
    

    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        obj.code = generator(length=6)
        obj.save()
        return super().response_add(request, obj, post_url_continue)
    
    def save_model(self, request, obj, form=None, change=None) -> None:
        service =  obj.services
        if service.function != None:
            data = {
                'up':service.up,'ebb':service.ebb, 'efb':service.efb,'nb':obj.nb,'nf':obj.nf,
                'mncb':service.mncb, 'mncf':service.mncf,'ns':obj.ns
            }
            func = {
                'function1':function1(data),
                'general_engine_calc':general_engine_calc(data),
            }
            result = func.get(service.function)
            obj.total = result
        return super().save_model(request, obj, form, change)

        