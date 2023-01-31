from django.contrib import admin
from realestate.models import *
# Register your models here.


@admin.register(RealEstate)
class realestateAdmin(admin.ModelAdmin):
    list_display = ['name','total_amount','amount_deposited','unit_price','created_at']
    # search_fields = ['student__startswith', 'year__startswith']
    list_filter = ['name','created_at']
    # actions = [filter_student]



@admin.register(RealEstatePlot)
class realestatePlotAdmin(admin.ModelAdmin):
    list_display = ['realestate','name','price','size','created_at']
    # search_fields = ['student__startswith', 'year__startswith']
    list_filter = ['realestate','name','created_at']