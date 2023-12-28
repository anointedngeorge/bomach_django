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
import uuid


import os
import sys
sys.path.append(os.path.abspath('../../bomach_django'))

@admin.register(User)
class AuthModelAdmin(admin.ModelAdmin):
    # search_fields = ['username__startswith', 'code__startswith']
    list_display = ['pk']
    # actions = [send_bulk_message, approve_bulk, reject_bulk]
    form = userRegistrationForm

    
    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        coded = str(uuid.uuid4()).replace("-", "")[:4]
        code = f"bom{coded}"
        obj.code = code
        obj.save()
        return super().response_add(request, obj, post_url_continue)
    
