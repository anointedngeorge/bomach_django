from django.contrib import admin
from customer.models import *
# Register your models here.


@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    pass