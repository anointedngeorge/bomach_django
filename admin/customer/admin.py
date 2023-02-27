from django.contrib import admin
from customer.models import *
import uuid
# Register your models here.
from plugins.generator import generator

@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ['user']
    exclude = ['user','code']

    def has_add_permission(self, request) -> bool:
        return False

    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generator()
        obj.save()
        return super().response_add(request, obj, post_url_continue)