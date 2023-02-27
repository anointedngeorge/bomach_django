from django.contrib import admin
from realestate.models import *
from django.urls import path, reverse
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from django.contrib import messages as messag
from customer.models import *
from django.shortcuts import redirect
from django.conf import settings
import uuid
from plugins.generator import generator



PATH_URI = settings.ADMIN_URI


@admin.register(RealEstate)
class RealestateAdmin(admin.ModelAdmin):
    list_display = ['user','branch','name','unit_price', 'survey_plan','legal_fee','development_fee', 'created_at','action']
    # search_fields = ['student__startswith', 'year__startswith']
    list_filter = ['name','created_at']
    exclude = ['code']
    # actions = [filter_student]
 
    fieldsets = (
      ('Realestate Details', {
          'fields': ('branch','name')
      }),
      ('Quantity Price', {
          'fields': ('unit_price','legal_fee', 'survey_plan', 'development_fee')
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
    
    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generator()
        obj.save()
        return super().response_add(request, obj, post_url_continue)


    def save_model(self, request, obj, form, change) -> None:
        logged_user = request.user
        obj.user = logged_user
        return super().save_model(request, obj, form, change)




