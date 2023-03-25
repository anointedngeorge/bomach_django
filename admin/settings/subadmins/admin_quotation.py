from django.contrib import admin

# Register your models here.

from settings.submodels.model_gallery import *
from settings.submodels.model_service import *
from settings.submodels.quotation_model import *



@admin.register(Quotation)
class ActivitiesAdmin(admin.ModelAdmin):
    pass



@admin.register(LaborBillQuotation)
class LaborBillQuotationAdmin(admin.ModelAdmin):
    
    class Media:
        js = (
            'custom/jquery-3.6.4.min.js', 
            'custom/app.js',       # project static folder
          
        )