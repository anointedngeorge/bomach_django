import importlib
from django import template
from django.core import serializers
from django.utils.html import format_html
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.contrib.admin.templatetags.admin_list import result_headers, result_hidden_fields, ResultList, \
    items_for_result
from django.contrib.admin.templatetags.base import InclusionAdminNode
from plugins.word_transform import is_camel_or_pascal_case
import re



register = template.Library()


@register.simple_tag
def show_count(object, **kwargs):
    '''
        Using the importlib to import relative object path.
        this will have some filter arguments from kwargs.
    '''
    try:
        module_name, class_name = object.rsplit('.', 1)
        module = importlib.import_module(module_name)
        app_obj = getattr(module, class_name)
        if len(kwargs) > 0:
            app = app_obj.objects.all().filter(**kwargs)
            return app.count()
        else:
            app = app_obj.objects.all()
            return app.count()
    except Exception as e:
        return f"{e}"
    


@register.simple_tag
def show_filtered_data(object=None, order_by='created', **kwargs):
    if object == None:
        return "Object can not be None."
    try:
        module_name, class_name = object.rsplit('.', 1)
        module = importlib.import_module(module_name)
        app_obj = getattr(module, class_name)
        if len(kwargs) > 0:
            app = app_obj.objects.all().filter(**kwargs).order_by(order_by)
            return app
    except Exception as e:
        return f"{e}"


@register.simple_tag
def show_data_list(object=None, limit=6, order_by='created' ):
    try:
        module_name, class_name = object.rsplit('.', 1)
        module = importlib.import_module(module_name)
        app_obj = getattr(module, class_name)
        app = app_obj.objects.all().order_by(order_by)
        app = app[:limit]
        return app
    except Exception as e:
        return f"{e}"
    


@register.simple_tag
def show_table_data(queryset=[], head='', fields='', classattrs='table'):
     
    if len(queryset) < 1:
        return format_html(f"<b>{len(queryset)} Empty</b>")
    
    try:
        table =""
        table +="<div class='table-responsive'>"
        table += f"<table class='{classattrs}'>"
        field =  fields.split(",") if fields.__contains__(",") else  fields.split(' ')
        counter = 1

        table += "<thead>"
        table += f"<tr>"
        table += f"<th> # </th>"
        for fi in field:
            fm = str(fi).replace("_", " ").upper()
            table += f"<th> {fm} </th>"
        table += "</tr>"
        table += "<thead>"
        table += "<tbody>"
        for x in queryset:
            # print(x)
            table += f"<tr>"
            table += f"<td> {counter}: </td>"
            for fi in field:
                data_set = eval(f"x.{fi}")
                table += f"<td> {data_set} </td>"
            table += "</tr>"
            counter = counter + 1
        table += "</tbody>"
        table += "</table>"
        table +="</div>"
        return format_html(table)
    except Exception as e:
        return f"{e}"



def results(cl):
    if cl.formset:
        for res, form in zip(cl.result_list, cl.formset.forms):
            yield (res, ResultList(form, items_for_result(cl, res, form)))
    else:
        for res in cl.result_list:
            result = (res, ResultList(None, items_for_result(cl, res, None)))
            result2 = ResultList(None, items_for_result(cl, res, None))
            yield result2




FILENAME = 'admin/change_list_results.html'
@register.inclusion_tag(filename=FILENAME, takes_context=True)
def custom_result_list(context, cl):
    headers = list(result_headers(cl))
    num_sorted_fields = 0
    for h in headers:
        if h['sortable'] and h['sorted']:
            num_sorted_fields += 1

    return {
        'cl': cl,
        'result_hidden_fields': list(result_hidden_fields(cl)),
        'result_headers': headers,
        'num_sorted_fields': num_sorted_fields,
        'results': list(results(cl)),
    }





@register.simple_tag
def is_camel_or_pascal_case(word='testWord'):
    # Check if the word is in camel-case or Pascal-case
    # print(word)
    return re.match(r'^[a-z]+(?:[A-Z][a-z]*)*$', word) is not None




'''
apply_select_related
can_show_all
clear_all_filters_qs
date_hierarchy
filter_specs
formset
full_result_count
get_filters
get_filters_params
get_ordering
get_ordering_field
get_ordering_field_columns
get_query_string
get_queryset
get_results
has_active_filters
has_filters
has_related_field_in_list_display
is_popup
list_display
list_display_links
list_editable
list_filter
list_max_show_all
list_per_page
list_select_related
lookup_opts
model
model_admin
multi_page
opts
page_num
paginator
params
pk_attname
preserved_filters
query
queryset
result_count
result_list
root_queryset
search_fields
search_form_class
search_help_text
show_admin_actions
show_all
show_full_result_count
sortable_by
title
to_field
url_for_result

'''