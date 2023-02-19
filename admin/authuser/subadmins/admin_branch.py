from django.contrib import admin
from django.contrib.admin.sites import site
from django.http import request
from django.http.response import HttpResponse
from django.template.response import TemplateResponse
from django.urls import path
from authuser.models import * 
from authuser.forms import *
from django.shortcuts import render
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.html import format_html
from django.utils.safestring import mark_safe
# from etc.actions import *

from django.http import HttpResponseRedirect
from django import template
# from django.utils.translation import ugettext as _



@admin.register(Branch)
class BranchModel(admin.ModelAdmin):
    search_fields = ['name__startswith']
    list_display = ['name','country','state','office_address','no_of_staff','branch_date']
    list_filter = ['name']


@admin.register(BranchAccessories)
class BranchAccessoriesModel(admin.ModelAdmin):
    search_fields = ['name__startswith']
    list_display = ['name','image','serial_number']
    list_filter = ['name']