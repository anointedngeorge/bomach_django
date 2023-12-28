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

@admin.register(RealEstatePayment)
class RealesteatePaymentAdmin(admin.ModelAdmin):
   
    list_display = ['created_at','plot','status','activation_code','customer_email','purchase_code','customer','initial_amount','limited_date']
    # search_fields = ['student__startswith', 'year__startswith']
    list_filter = ['customer_email','customer','created_at']
    exclude = ['code']
    
    # def has_add_permission(self, request) -> bool:
    #     return False

    # def has_change_permission(self, request, obj=None) -> bool:
    #     return False


