import os
import sys
sys.path.append(os.path.abspath('../../bomach_django'))

from typing import Any, Dict, List, Optional
from django.http import HttpResponse
from django.contrib import messages as mesage
from django.contrib import admin
from django.shortcuts import redirect
from django.urls.resolvers import URLResolver
from django.urls import path, include, re_path
from django.template.response import TemplateResponse
from django.contrib.auth import views as auth_views
# from plugins.django_pdf import generate_pdf
from dashboard.forms.authentication import (
    CustomAuthenticationForm,
    AuthenticationRegisterForm
)
from authuser.models import *
import importlib

import os
from plugins.logging import CreateErrorLog
# import logic files



CURRENT_ADMIN = 'staff'
CURRENT_MAIN_TEMPLATE = 'admin'


class StaffDashboard(admin.AdminSite):
    site_title = 'Bomach Staff Dashboard'
    site_header = 'Staff Dashboard'
    index_title = 'Bomach Staff'
    login_title = 'Bomach Staff Login'
    footer_description = """
                        Bomach - Bootstrap Staff Template by
                        <a href="https://colorlib.com">Colorlib</a>
                        """
    index_template = f'{CURRENT_MAIN_TEMPLATE}/index.html'
    login_template = f'{CURRENT_MAIN_TEMPLATE}/login.html'
    logout_template = f'{CURRENT_MAIN_TEMPLATE}/logout.html'
    login_form = CustomAuthenticationForm

    

    def each_context(self, request):
        context = super().each_context(request)
        app_lists = self.get_app_list(request)
        
        context['title'] = self.site_title
        context['site_header'] = self.site_header
        context['index_title'] = self.index_title
        context['app_lists'] = app_lists
        context['login_title'] = self.login_title
        # this will set the current adminsite app that is running
        context['adminsite'] = self.name
        context['MAIN_TEMPLATE'] = CURRENT_MAIN_TEMPLATE
        context['footer_description'] = self.footer_description
        return context
    
    def get_urls(self) -> List[URLResolver]:
        urls = super().get_urls()
        add_urls = [
            path('profile/<str:id>/', self.profile, name='profile'),

            # path('generate_pdf/', self.custom_generate_pdf, 
            #                 name='generate_pdf'),

            path('views/<str:id>/<str:function_name>/', self.views, 
                            name='views'),
            path('add/<str:id>/<str:function_name>/', self.add, 
                            name='add'),
            path('edit/<str:id>/<str:function_name>/', self.edit, 
                            name='edit'),
            path('tasks/<str:id>/<str:function_name>/', self.tasks,
                            name='tasks'),
        ]
        return add_urls + urls

    
    def profile(self, request, id=None):
        context = dict(self.each_context(request),)
        context['title'] = f"Profile {id} "
        context['site_header'] = f"Edit Profile"
        context['site_title'] = f"m"
        return TemplateResponse(request, f'{CURRENT_MAIN_TEMPLATE}/profile.html', context)


    def views(self, request, id=None, function_name=None, template=None):
        '''This module will be used to import all logic related to views'''
        import importlib
        module_name = 'superadmin.business_logic.views' 

        try:
            module = importlib.import_module(module_name)
            if hasattr(module, function_name):
                function = getattr(module, function_name)
                foundFunction = function(request, id=id, current_template=CURRENT_MAIN_TEMPLATE)
                return foundFunction
            else:
                return HttpResponse(f"The function {function_name} does not exist in the module.")
        except Exception as e:
            CreateErrorLog(e)
            # print(f"Failed to import the module {module_name}.")
        return HttpResponse(f"The function does not exist in the module.")


    def add(self, request, id=None, function_name=None, template=None):
        '''This module will be used to import all logic related to add'''
        import importlib
        module_name = 'superadmin.business_logic.add' 

        try:
            module = importlib.import_module(module_name)
            if hasattr(module, function_name):
                function = getattr(module, function_name)
                foundFunction = function(request, id=id, current_template=CURRENT_MAIN_TEMPLATE)
                
                return foundFunction
            else:
                return HttpResponse(f"The function {function_name} does not exist in the module.")
        except Exception as e:
            CreateErrorLog(e)
            # print(f"Failed to import the module {module_name}.")
        return HttpResponse(f"The function does not exist in the module.")


    def edit(self, request, id=None, function_name=None, template=None):
        '''This module will be used to import all logic related to edit'''
        import importlib
        module_name = 'superadmin.business_logic.edit' 

        try:
            module = importlib.import_module(module_name)
            if hasattr(module, function_name):
                function = getattr(module, function_name)
                foundFunction = function(request, id=id, current_template=CURRENT_MAIN_TEMPLATE)
                return foundFunction
            else:
                return HttpResponse(f"The function {function_name} does not exist in the module.")
        except Exception as e:
            # print(e)
            CreateErrorLog(e)
            # print(f"Failed to import the module {module_name}.")
        return HttpResponse(f"The function does not exist in the module.")

    

    def tasks(self, request, id=None, function_name=None, template=None):
        '''This module will be used to import all logic related to edit'''
        import importlib
        module_name = 'superadmin.business_logic.task' 

        try:
            module = importlib.import_module(module_name)
            if hasattr(module, function_name):
                function = getattr(module, function_name)
                foundFunction = function(request, id=id, current_template=CURRENT_MAIN_TEMPLATE)
                return foundFunction
            else:
                return HttpResponse(f"The function {function_name} does not exist in the module.")
        except Exception as e:
            CreateErrorLog(e)
            # print(f"Failed to import the module {module_name}.")
        return HttpResponse(f"The function does not exist in the module.")

    # def custom_generate_pdf(self, request):
    #     generatePdf = generate_pdf(
    #         request=request,
    #         context={},
    #         template_path='pdf/test_pdf.html',
    #         template_name='testPdf'
    #     )
    #     return generatePdf
    

staff_dashboard_site = StaffDashboard(name=CURRENT_ADMIN)

# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
