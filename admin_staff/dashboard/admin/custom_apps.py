import importlib
from typing import Any
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.db.models.query import QuerySet
from django.http import HttpRequest
import os
from django.forms import formset_factory
from dashboard.admin import CURRENT_MAIN_TEMPLATE, CURRENT_ADMIN, staff_dashboard_site
from dashboard.admin.registered_apps_list import REGISTERED_APP

TEMPLATE_PATHS = {
    'list_template': 'change_list.html',
    'form_template': 'change_form.html',
    'delete_confirmation_template': 'delete_confirmation_template.html',
}

def get_template_path(app_label, model_name, template_type):
    template_path = os.path.realpath(
        # f'{CURRENT_ADMIN}/templates/{CURRENT_MAIN_TEMPLATE}/{app_label}/{model_name}/{TEMPLATE_PATHS[template_type]}'
        f'{CURRENT_MAIN_TEMPLATE}/{app_label}/{model_name}/{TEMPLATE_PATHS[template_type]}'
    )
    return template_path if os.path.exists(template_path) else f'{CURRENT_MAIN_TEMPLATE}/{TEMPLATE_PATHS[template_type]}'

try:
    for app in REGISTERED_APP:
        
        module_name, class_name = app.rsplit('.', 1)
        
        module = importlib.import_module(module_name)
        app_obj = getattr(module, class_name)
        
      
        list_display = app_obj.list_display(None) if hasattr(app_obj,"list_display") else ['pk']
        list_filter = app_obj.list_filter(None) if hasattr(app_obj,"list_filter") else []
        list_display_links = app_obj.list_display_links(None) if hasattr(app_obj,"list_display_links") else ['pk']
        exclude = app_obj.exclude(None) if hasattr(app_obj,"exclude") else []
        has_action = app_obj.has_action(None) if hasattr(app_obj,"has_action") else False
        is_registered = app_obj.is_registered(None) if hasattr(app_obj,"is_registered") else False
        list_form = app_obj.list_form(None) if hasattr(app_obj,"list_form") else "__all__"
        # customform= app_obj.form(None) if hasattr(app_obj,"form") else None
        form_app =  False
        
        # print(check_attr_state)
        if is_registered:

            class CustomAdminSite(admin.ModelAdmin):
                list_display = ['action'] + list_display if has_action else list_display
                list_display_links = list_display_links
                list_filter = list_filter
                list_form = list_form
                exclude = exclude

                if hasattr(app_obj,"form"):
                    form = app_obj.form(None)
                  
    
                MODEL = app_obj
                m = MODEL._meta

                delete_confirmation_template = get_template_path(m.app_label, m.model_name, 'delete_confirmation_template')
                change_list_template = get_template_path(m.app_label, m.model_name, 'list_template')
                change_form_template = get_template_path(m.app_label, m.model_name, 'form_template')
                
            
                def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
                    queryset = super().get_queryset(request)
                    return queryset if request.user.is_superuser else queryset.filter(id=request.user.id)

                
                def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
                    if extra_context is None:
                        extra_context = {}

                    extra_context['referer'] = request.META.get('HTTP_REFERER')
                    extra_context['page_title'] = self.m.verbose_name

                    return super().changeform_view(request, object_id, form_url, extra_context)
                

                def changelist_view(self, request, extra_context=None):
                    if extra_context is None:
                        extra_context = {}
                    extra_context['referer'] = request.META.get('HTTP_REFERER')
                    extra_context['page_title'] = self.m.verbose_name
                    
                    return super().changelist_view(request, extra_context=extra_context)


                def get_form(self, request: Any, obj, change=None, **kwargs) -> Any:
                    return super().get_form(request, obj, change, **kwargs)

                
                def get_changelist(self, request: HttpRequest, **kwargs):
                    return super().get_changelist(request, **kwargs)
                
            staff_dashboard_site.register(app_obj, CustomAdminSite)

except Exception as e:
    from plugins.logging import CreateErrorLog
    CreateErrorLog(e)

