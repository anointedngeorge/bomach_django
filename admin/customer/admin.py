from django.contrib import admin
from customer.models import *
# Register your models here.


@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ['user']
    exclude = ['user']

    def has_add_permission(self, request) -> bool:
        return False