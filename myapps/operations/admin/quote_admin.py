from django.contrib import admin
from operations.models import *
from plugins.calculator import *
from plugins.code_generator import generateUniqueId
from django.http import HttpResponse
from actions.serviceQuote import *
from system_functions.engineering_function import *


@admin.register(QuotesModel)
class QuotesModelAdmin(admin.ModelAdmin):
    list_display = ['code','customer','services','nb','nf','ns','total','status','action']
    exclude = ['total','code','amount_deposited','amount_pending']
    actions = [ViewProfileAction, viewQuoteOrders]
    
    def get_urls(self):
        qs = super().get_urls()    
        urlpatterns = [
            path('update-status/<int:id>/<str:status>/<str:function>',self.updateStatus, 
            name='update-status'),
            path('make-payment/<int:id>',self.makePayment, 
            name='make-payment')
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

    def makePayment(self, request, id=None):
        context ={}
        context['id'] = id
        return TemplateResponse(request, 'templateResponse/make_payment.html', context=context)


    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        obj.code = generateUniqueId(length=6)
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

        