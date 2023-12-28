from django.contrib import admin
from customer.models import *
import uuid
# Register your models here.
from plugins.generator import generator
from actions.generator import codeGenerator
from actions.clientActions import *


@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    list_display = CUSTOMER_ADMIN_LIST
    exclude = ['code']
    actions = [SendMessage,ViewProfileAction,viewDataInPDF ,codeGenerator]

    def has_add_permission(self, request) -> bool:
        if not request.user.is_superuser:
            return False
        return True

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = queryset.filter(user_id=request.user.id)
            return qs
        return queryset

    def response_add(self, request, obj, post_url_continue=None):
        obj.code = generator()
        obj.save()
        return super().response_add(request, obj, post_url_continue)