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



@admin.register(User)
class AuthModelAdmin(admin.ModelAdmin):
    search_fields = ['username__startswith', 'code__startswith']
    list_display = ['username','code', 'first_name','last_name', 'email','roles','roles_name','is_active','is_staff','is_superuser']
    list_filter = ['first_name','roles_name',]
    # actions = ['']
    exclude = ['code','last_login','is_superuser','user_permissions',]
    # actions = [send_bulk_message, approve_bulk, reject_bulk]
    form = userRegistrationForm
    

    def response_post_save_add(self, request, obj):
        try:
            current_site = get_current_site(request)
            # data = { 'user': obj.email, 'domain': current_site.domain, 'uid': urlsafe_base64_encode(force_bytes(obj.id)) }
            data = { 'user': obj.email, 'domain': current_site.domain}
            mail_subject = 'Account Creation...'
            message = render_to_string('email_template/welcome.html', data)
            to_email = f"{obj.email}"
            test_email = 'demo@gmail.com'
            email = EmailMessage(mail_subject, message, to=[to_email], from_email=f'Anointed <{test_email}>')
            email.send()
            return super().response_post_save_add(request, obj)
        except Exception as e:
             print(e)


    
    def save_model(self, request, obj, form, change) -> None:
        if len(obj.password) > 70:
            pass
        else:
            obj.set_password(obj.password)
        obj.is_active = True
        return super().save_model(request, obj, form, change)
    

    

@admin.register(Staff)
class StaffModel(admin.ModelAdmin):
    search_fields = ['user__startswith']
    list_display = ['user']
    list_filter = ['user']



@admin.register(Customer)
class ClientModel(admin.ModelAdmin):
    search_fields = ['user__startswith']
    list_display = ['user']
    list_filter = ['user']