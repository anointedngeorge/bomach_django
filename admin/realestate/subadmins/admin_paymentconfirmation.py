from django.contrib import admin
from realestate.models import *
from django.urls import path, reverse
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from django.contrib import messages as messag
from customer.models import *
from django.shortcuts import redirect
from django.conf import settings

PATH_URI = settings.ADMIN_URI



@admin.register(PaymentConfirmationRequest)
class PaymentConfirmation(admin.ModelAdmin):
    list_display = ['created_at','payment','user','activation_code','activation_link','activation_link_code']