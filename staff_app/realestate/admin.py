from django.contrib import admin
from realestate.models import *
from django.urls import path, reverse
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from django.contrib import messages as messag
from customer.models import *



@admin.register(RealEstate)
class realestateAdmin(admin.ModelAdmin):
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
class realestatePlotAdmin(admin.ModelAdmin):
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
    
        ]
        return new_url + urls


    def sell_plot(self, request):
        context = dict(self.admin_site.each_context(request),)
        # grab query parameters
        query = request.GET.dict()
        id = int(query.get('id'))
        customers = Customer.objects.all()
        context['title'] = 'Sell '
        context['page_title'] = query.get('title')
        context['id'] = id
        context['customers'] = customers

        return TemplateResponse(request, 'templateResponse/sell_plot.html', context=context)

        
    def get_queryset(self, request):
        user =  request.user
        if not user.is_superuser: 
            return self.model.objects.all().filter(user=user)
        else:
            return   super().get_queryset(request)

    def save_model(self, request, obj, form, change) -> None:
        logged_user = request.user
        if obj.user != None:
            pass
        else: obj.user = logged_user
        return super().save_model(request, obj, form, change )