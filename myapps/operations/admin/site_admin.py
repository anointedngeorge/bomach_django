from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Register your models here.
# from fpdf import FPDF
from plugins.pdf import convert_to_file_to_pdf

from operations.models import *
import uuid
from plugins.code_generator import generateUniqueId
from plugins.dropdown import dictDropdown




@admin.register(OperationSite)
class OperationSiteAdmin(admin.ModelAdmin):
   
    list_display = ['site_code','user','site_name','date_creation','service_category','site_client']
    
    exclude = ['code','site_code']

    fieldsets = (
      ('Site Details', {
          'fields': ('site_name','date_creation','service_category','status','site_client','site_country',
          'site_state', 'site_lga',)
      }),
      
      ('Other', {
          'fields': ('site_map_location','scope_of_work','project',)
      }),
      
      ('Add Store', {
          'fields': ('stores',)
      }),
   )
    def response_add(self, request, obj, post_url_continue=None):
        code1 = f"{str(obj.site_client.user.surname)[:1]}{str(obj.site_client.user.first_name)[1]}{str(obj.site_client.user.last_name)[:1]}"
        code2 = f"{str(obj.site_state)[:1]}/{str(obj.site_lga).replace(' ','')}"
        site_code = f"{code1}/{code2}/s{obj.id}".upper()
        obj.site_code = site_code
        obj.code = generateUniqueId()
        obj.user = request.user
        obj.save()
        related_stores =  obj.stores.all()
        for e in related_stores:
            e.site_code = obj.site_code
            e.is_site_taken = True  
            e.save()

        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj) -> HttpResponse:
        related_stores =  obj.stores.all()
        store =  Stores.objects.all()
        get_store_data = store.filter(site_code=obj.site_code)
        # this will check if get_store_data has existing data inside,
        # then will turn all to false.
        
        if len(get_store_data) > 0:
            for x in get_store_data:
                x.is_site_taken = False
                x.site_code = ''
                x.save()

            # if the first argument runs succeessfully, the second argument 
            # will execute.
            if len(related_stores) > 0:
                for e in related_stores:
                    e.is_site_taken = True
                    e.site_code = obj.site_code
                    e.save()
        else:
            for e in related_stores:
                e.is_site_taken = True
                e.site_code = obj.site_code
                e.save()


           
        return super().response_change(request, obj)


    



