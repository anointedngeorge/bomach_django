from django.contrib import admin

# Register your models here.

from reports.models import *

@admin.register(ReportPayment)
class PaymentAdmin(admin.ModelAdmin):
    pass