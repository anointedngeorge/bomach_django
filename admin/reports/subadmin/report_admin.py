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
from reports.submodel.report_model import ReportingSheet



@admin.register(ReportingSheet)
class ReportingAdmin(admin.ModelAdmin):
    list_display = ['author','modelname']
    exclude = ['author','modelname','modelid']

    def has_add_permission(self, request) -> bool:
        return False