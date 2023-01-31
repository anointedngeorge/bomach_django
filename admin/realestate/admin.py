from django.contrib import admin
from realestate.models import *
# Register your models here.


@admin.register(RealEstate)
class realestateAdmin(admin.ModelAdmin):
    pass



@admin.register(RealEstatePlot)
class realestatePlotAdmin(admin.ModelAdmin):
    pass