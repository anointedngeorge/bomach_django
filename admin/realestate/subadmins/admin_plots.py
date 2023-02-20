from django.contrib import admin
from realestate.models import *
from django.urls import path, reverse
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from django.contrib import messages as messag
from customer.models import *
from django.shortcuts import redirect
from django.conf import settings

PATH_URI = settings.ADMIN_URI



@admin.register(RealEstatePlot)
class RealestatePlotAdmin(admin.ModelAdmin):
    ated_at = models.DateField(auto_now=True)
   
    list_display = ['created_at','user','realestate','name','price','size','purchase_code','status','action']
    # search_fields = ['student__startswith', 'year__startswith']
    list_filter = ['realestate','name','created_at','purchase_code']
    fieldsets = (
      ('Plot Form', {
          'fields': ('realestate','name',)
      }),
      ('Quantity Price', {
          'fields': ('size','status',)
      }),
   )

    def get_urls(self):
        urls = super().get_urls()
        # path('sell-plot', for urls with queries ?id=2
        new_url = [
            path('invoice/<int:id>/', self.admin_site.admin_view(
                self.invoice), name="invoice"),

            path('sell-plot', self.admin_site.admin_view(
                self.sell_plot), name="sell-plot"),

            path('activate-payment/<int:id>/', self.admin_site.admin_view(
                self.activate_payment), name="activate-payment"),

            path('confirm-payment', self.admin_site.admin_view(
                self.confirm_payment), name="confirm-payment"),

            path('search-payment-activation-code/<int:id>/', self.admin_site.admin_view(
                self.search_payment_activation_code), name="search-payment-activation-code"),
            

            path('change-plot-ownership', self.admin_site.admin_view(
                self.change_plot_ownership), name="change-plot-ownership"),
            
            path('selling-page/<str:pagename>/<int:id>/<str:amount>/', self.admin_site.admin_view(
                self.selling_page), name="selling-page"),

            path('test-page/', self.admin_site.admin_view(
                self.test_page), name="test-page"),
            
            path('admin-confirm-payment/<str:code>/', self.admin_site.admin_view(
                self.admin_confirm_payment), name="admin-approve-payment"),

            path('admin-approve-payment/<str:code>/<int:user_id>/', self.admin_site.admin_view(
                self.admin_approve_payment), name="admin-approve-payment"),
                
        ]
        return new_url + urls

    
    
    def invoice(self, request, id=None):
        context = dict(self.admin_site.each_context(request),)
        context['id'] = id
        context['site_title'] = 'Invoice'
        context['title'] =  'Invoice'
        
        return TemplateResponse(request, f"templateResponse/realestate/invoice.html", context=context)

    def admin_confirm_payment(self, request, code=None):
        """
        This will serve as a link to confirmation page.
        """
        user =  request.user.id
        http =  request.META.get('wsgi.url_scheme')
        host =  request.META.get('HTTP_HOST')
        data = {'id':code}
        payment =  RealEstatePayment.objects.all()
        plot_content  = RealEstatePlot.objects.all()
        if payment.filter(**data).exists():
           payment = payment.filter(**data).get()
           activation_code =  payment.activation_code

           URL =  f"{http}://{host}{PATH_URI}/realestate/realestateplot/admin-approve-payment/{activation_code}/{user}/"
           URL2 =  f"{http}://{host}{PATH_URI}/realestate/realestateplot/admin-payment-status/{activation_code}/"
           confirmBox = PaymentConfirmationRequest.objects.all()
           
           if not confirmBox.filter(activation_code=activation_code).exists():
                data3 = {'status':'waiting'}
                plot =  plot_content.filter(id=payment.plot.id).update(**data3)
                plot_with_id =  plot_content.filter(id=payment.plot.id).get()
               
                # if payment.plot.id == plot_with_id.id:
                data2 = {
                    'activation_code':activation_code,
                    'activation_link':URL,
                    'payment_id':code,
                    'user_id':user,
                    'activation_link_code':URL2,
                }
                confirmBox.create(**data2)
                
           else:
               return HttpResponse("Already Confirmed!")

        #    messag.success(request, f"Use this link to check status, {URL2}.")
           return HttpResponse(f"Check status: {URL2}")

    def admin_approve_payment(self, request, code=None):
        """
        This will serve as a confirmation link.
        """
        URL =  f"{PATH_URI}"
        return HttpResponse(URL)

    
    def selling_page(self, request, pagename=None, id=None, amount=None):
        context = {}
        context['id'] = id
        context['amount'] = amount
        return TemplateResponse(request, f"templateResponse/realestate/{pagename}.html", context=context)
        # return HttpResponse('Yes')


    def test_page(self, request):
        return HttpResponse('Yes')

    def change_plot_ownership(self, request):
        context = dict(self.admin_site.each_context(request),)
        query = request.GET.dict()
        id = int(query.get('id'))
        context['title'] = 'Change Ownership'
        context['page_title'] = query.get('title')

        return TemplateResponse(request, 'templateResponse/realestate/change_ownership.html', context=context)

    def search_payment_activation_code(self, request, id=None):
        context = {}
        activate_code = request.GET['activation_code']
        payment =  RealEstatePayment.objects.all().filter(activation_code=activate_code, plot_id=id)
        if payment:
            context['payment'] = payment.get()
            return TemplateResponse(request, 'templateResponse/realestate/payment_confirmation_page.html', context=context)
        else: 
            return HttpResponse('Activation code does not exist or you put a wrong activation code.')

    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        estate_total_amount =  float(obj.realestate.unit_price) * float(obj.size)
        extra_fees =  float(obj.realestate.survey_plan) + float(obj.realestate.development_fee) + float(obj.realestate.legal_fee)
        obj.price = float(estate_total_amount) + float(extra_fees)
        obj.save()
        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj) -> HttpResponse:
        estate_total_amount =  int(obj.realestate.unit_price) * int(obj.size)
        extra_fees =  int(obj.realestate.survey_plan) + int(obj.realestate.development_fee) + int(obj.realestate.legal_fee)
        obj.price = int(estate_total_amount) + int(extra_fees)
        obj.save()
        return super().response_change(request, obj)

    def confirm_payment(self, request, id=None):
        context = dict(self.admin_site.each_context(request),)
        query = request.GET.dict()
        id = int(query.get('id'))
        context['title'] = 'Confirm Payment'
        context['page_title'] = query.get('title')
        context['id'] = id
        plot_payment =  RealEstatePayment.objects.all().filter(plot_id = id)
        if plot_payment.exists():
            if plot_payment.get().is_confirmed:
                return HttpResponse("Plot Already Confirmed")
            
        return TemplateResponse(request, 'templateResponse/realestate/confirm_payment.html', context=context)


    def sell_plot(self, request):
        context = dict(self.admin_site.each_context(request),)
        # grab query parameters
        query = request.GET.dict()
        id = int(query.get('id'))
        customers = Customer.objects.all()
        context['title'] = 'Sell '
        context['page_title'] = query.get('title')
        context['id'] = id
        plot =  RealEstatePlot.objects.all()
        if plot.filter(id=id).exists():
            context['plot'] = plot.filter(id=id).get()
            return TemplateResponse(request, 'templateResponse/realestate/sell_plot.html', 
            context=context)
        return HttpResponse("Failed to load pages")


    def activate_payment(self, request, id=None):
        data =  request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        user_id =  request.user.id
        
        
        payment = RealEstatePayment.objects.all()
        if not payment.filter(plot_id=id).exists():
            RealEstatePlot.objects.all().filter(id=id).update(status=data.get('status'))
            data.update({'user_id':user_id, 'plot_id':id})
            payment.create(**data)
            messag.success(request, "Payment Activated")
        else:
            dd = payment.filter(plot_id=id).get()
            messag.error(request, f"Payment already made for {dd.plot.name}")
        return redirect(request.META.get('HTTP_REFERER'))

    def get_queryset(self, request):
        user =  request.user
        if not user.is_superuser: 
            return self.model.objects.all().filter(user=user)
        else:
            return super().get_queryset(request)

    def save_model(self, request, obj, form, change) -> None:
        logged_user = request.user
        if obj.user != None:
            pass
        else: obj.user = logged_user
        return super().save_model(request, obj, form, change )




