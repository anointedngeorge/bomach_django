from django.contrib import admin
from realestate.models import *
from django.urls import path, reverse
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from django.contrib import messages as messag
from customer.models import *
from django.shortcuts import redirect
from django.conf import settings
import uuid

# Register your models here.
from reports.models import *

@admin.register(ReportPayment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['author','client','total_amount','code']
    exclude = ['code']

    def has_add_permission(self, request) -> bool:
        return False

    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        code = uuid.uuid4().hex
        obj.code = code
        obj.save()
        return super().response_add(request, obj, post_url_continue)