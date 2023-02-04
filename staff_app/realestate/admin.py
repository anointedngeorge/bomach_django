from django.contrib import admin
from realestate.models import *
# Register your models here.


@admin.register(RealEstate)
class realestateAdmin(admin.ModelAdmin):

    list_display = ['user','branch','name','total_amount','amount_deposited','unit_price','created_at']
    # search_fields = ['student__startswith', 'year__startswith']
    list_filter = ['name','created_at']
    # actions = [filter_student]
 
    fieldsets = (
      ('Realestate Details', {
          'fields': ('branch','name',)
      }),
      ('Quantity Price', {
          'fields': ('total_amount', 'amount_deposited', 'unit_price')
      }),

      ('Extra Fees', {
          'fields': ('legal_fee', 'survey_plan', 'development_fee')
      }),
   )

    def get_queryset(self, request):
        user =  request.user
        if not user.is_superuser: 
            return self.model.objects.all().filter(user=user)
        else:
            return super().get_queryset(request)


    def changelist_view(self, request, extra_context=None) :
        
        return super().changelist_view(request, extra_context)
        # return super().changelist_view(request, extra_context

    def save_model(self, request, obj, form, change) -> None:
        logged_user = request.user
        obj.user = logged_user
        return super().save_model(request, obj, form, change)



@admin.register(RealEstatePlot)
class realestatePlotAdmin(admin.ModelAdmin):
    
    list_display = ['realestate','name','price','size','created_at']
    # search_fields = ['student__startswith', 'year__startswith']
    list_filter = ['realestate','name','created_at']
    