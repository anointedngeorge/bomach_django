import importlib
from typing import Any
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.db.models.query import QuerySet
from django.http import HttpRequest
import os
from django.forms import formset_factory
# from authuser.forms.user_form import AgentRegistrationForm
from payments.models.payments import DeliveryFeeCalculator
from dashboard.admin import CURRENT_MAIN_TEMPLATE, CURRENT_ADMIN, staff_dashboard_site
from dashboard.admin.registered_apps_list import REGISTERED_APP

TEMPLATE_PATHS = {
    'list_template': 'change_list.html',
    'form_template': 'change_form.html',
    'delete_confirmation_template': 'delete_confirmation_template.html',
}

def get_template_path(app_label, model_name, template_type):
    template_path = os.path.realpath(
        f'{CURRENT_MAIN_TEMPLATE}/templates/{CURRENT_ADMIN}/{app_label}/{model_name}/{TEMPLATE_PATHS[template_type]}'
    )
    return template_path if os.path.exists(template_path) else f'{CURRENT_ADMIN}/{TEMPLATE_PATHS[template_type]}'

try:
    for app in REGISTERED_APP:
        
        module_name, class_name = app.rsplit('.', 1)
        
        module = importlib.import_module(module_name)
        app_obj = getattr(module, class_name)
        
      
        list_display = app_obj.list_display(None) if hasattr(app_obj,"list_display") else ['pk']
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
                    from django.forms import modelform_factory
                    # to import model form
                    form_loader = modelform_factory(
                                        self.model, 
                                        fields=self.list_form, 
                                        exclude=self.exclude,
                                    )
                    queryset =  self.get_queryset(request)
                    
                    if extra_context is None:
                        extra_context = {}

                    extra_context['referer'] = request.META.get('HTTP_REFERER')
                    extra_context['page_title'] = self.m.verbose_name
                    form_in_use = form_loader(request.POST or 
                                            None, instance=queryset 
                                         .filter(id=object_id).get()) if object_id else form_loader
    
                    # will check if their is a custom for set:i.e if 
                    # form is not modelform, else use internal model form
                    if self.form.__name__ != 'ModelForm':
                        model_form = self.form(request.POST or 
                                            None, instance=queryset 
                                         .filter(id=object_id).get()) if object_id else self.form
                        extra_context['form'] = model_form
                    else:
                        extra_context['form'] = form_in_use

                    return super().changeform_view(request, object_id, form_url, extra_context)

                def get_form(self, request: Any, obj, change=None, **kwargs) -> Any:
                    return super().get_form(request, obj, change, **kwargs)

                # def changelist_view(self, request, extra_context=None):
                #     model = self.model
                #     ModelFormSet = formset_factory(self.get_changelist_formset(request), extra=0)
                #     formset = ModelFormSet()

                #     sortable_by = self.get_sortable_by(request) 
                #     search_help_text = self.get_search_fields(request)
                    
                #     for form in formset:
                #         form.queryset = model.objects.all()
                    
                #     cl = ChangeList(request, self.model, self.list_display, self.list_display_links, self.list_filter,
                #                     self.date_hierarchy, self.search_fields, self.list_select_related,
                #                     self.list_per_page, self.list_max_show_all, self.list_editable,
                #                     model_admin=self, sortable_by=sortable_by, search_help_text=search_help_text)
                    
                #     opts =  cl.model._meta
                #     if extra_context is None:
                #         extra_context = {}
                #     extra_context['referer'] = request.META.get('HTTP_REFERER')
                #     extra_context['cl'] = cl
                #     extra_context['formset'] = formset
                #     extra_context['opts'] = opts
                #     extra_context['page_title'] = opts.verbose_name
                    
                #     return super().changelist_view(request, extra_context=extra_context)

                def get_changelist(self, request: HttpRequest, **kwargs):
                    return super().get_changelist(request, **kwargs)
            staff_dashboard_site.register(app_obj, CustomAdminSite)

except Exception as e:
    from plugins.logging import CreateErrorLog
    CreateErrorLog(e)

