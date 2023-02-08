from django.contrib import admin
from realestate.models import *
from django.urls import path, reverse
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from django.contrib import messages as messag
from customer.models import *
from django.shortcuts import redirect



@admin.register(RealEstate)
class RealestateAdmin(admin.ModelAdmin):
    list_display = ['user','branch','name','total_amount','amount_deposited','unit_price','created_at','action']
    # search_fields = ['student__startswith', 'year__startswith']
    list_filter = ['name','created_at']
    # actions = [filter_student]
 
    fieldsets = (
      ('Realestate Details', {
          'fields': ('branch','name')
      }),
      ('Quantity Price', {
          'fields': ('total_amount', 'amount_deposited', 'unit_price')
      }),

      ('Extra Fees', {
          'fields': ('legal_fee', 'survey_plan', 'development_fee')
      }),

      ('Estate Status', {
          'fields': ('status',)
      }),
   )

    def get_queryset(self, request):
        user =  request.user
        if not user.is_superuser: 
            return self.model.objects.all().filter(user=user)
        else:
            return super().get_queryset(request)


    def save_model(self, request, obj, form, change) -> None:
        logged_user = request.user
        obj.user = logged_user
        return super().save_model(request, obj, form, change)



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
          'fields': ('price', 'size',)
      }),
      ('Plot Status', {
          'fields': ('status',)
      }),
   )
    def get_urls(self):
        urls = super().get_urls()
        # path('sell-plot', for urls with queries ?id=2
        new_url = [
            path('sell-plot', self.admin_site.admin_view(
                self.sell_plot), name="sell-plot"),

            path('activate-payment/<int:id>/', self.admin_site.admin_view(
                self.activate_payment), name="activate-payment"),

            path('confirm-payment', self.admin_site.admin_view(
                self.confirm_payment), name="confirm-payment"),
            path('search-payment-activation-code/', self.admin_site.admin_view(
                self.search_payment_activation_code), name="search-payment-activation-code"),
            

            path('change-plot-ownership', self.admin_site.admin_view(
                self.change_plot_ownership), name="change-plot-ownership"),
                
        ]
        return new_url + urls
    
    def change_plot_ownership(self, request):
        context = dict(self.admin_site.each_context(request),)
        query = request.GET.dict()
        id = int(query.get('id'))
        context['title'] = 'Change Ownership'
        context['page_title'] = query.get('title')
        return TemplateResponse(request, 'templateResponse/change_ownership.html', context=context)

    def search_payment_activation_code(self, request):
        activate_code = request.GET['activation_code']
        return HttpResponse(activate_code)

    def confirm_payment(self, request, id=None):
        context = dict(self.admin_site.each_context(request),)
        query = request.GET.dict()
        id = int(query.get('id'))
        context['title'] = 'Confirm Payment'
        context['page_title'] = query.get('title')
        context['id'] = id
        return TemplateResponse(request, 'templateResponse/confirm_payment.html', context=context)


    def sell_plot(self, request):
        context = dict(self.admin_site.each_context(request),)
        # grab query parameters
        query = request.GET.dict()
        id = int(query.get('id'))
        customers = Customer.objects.all()
        context['title'] = 'Sell '
        context['page_title'] = query.get('title')
        context['id'] = id
        return TemplateResponse(request, 'templateResponse/sell_plot.html', context=context)


    def activate_payment(self, request, id=None):
        data =  request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        user_id =  request.user.id
        data.update({'user_id':user_id, 'plot_id':id})
        RealEstatePlot.objects.all().filter(id=id).update(status=data.get('status'))
        payment = RealEstatePayment.objects.all()
        if not payment.filter(plot_id=id).exists():
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




@admin.register(RealEstatePayment)
class RealesteatePaymentAdmin(admin.ModelAdmin):
   
    list_display = ['created_at','plot','user','status','activation_code','customer_email','customer','initial_amount','limited_date']
    # search_fields = ['student__startswith', 'year__startswith']
    list_filter = ['customer_email','customer','created_at']
    
    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    