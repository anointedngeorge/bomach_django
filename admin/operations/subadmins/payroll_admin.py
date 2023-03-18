from django.contrib import admin
from operations.models import *
# from operations.submodels.store_model import Stores


@admin.register(PayRoll)
class PayrollAdmin(admin.ModelAdmin):
    pass
    # list_display = ['name', 'email', 'phone','branch']
