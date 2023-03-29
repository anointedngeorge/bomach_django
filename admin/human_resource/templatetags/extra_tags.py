from django import template
import json
from django.core import serializers
from django.utils import timezone
import datetime as dt
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import itertools
from operations.models import *

register = template.Library()


@register.simple_tag
def ListUlForSingleQuerySet(request=None, searchable_names='', queryset=None):
    data_header =  searchable_names.split(',')
    ul = ""

    try:
        ul += "<ul class='list-group list-group-flush'>"
        res=request.META

        serialized_data =  serializers.serialize('python', [queryset], use_natural_foreign_keys=True, use_natural_primary_keys=True) 
        for s in serialized_data:
            fields =  s.get('fields')
            for h in data_header:
                ul += f"<li class='list-group-item'><b>{str(h).replace('_',' ').title()}: </b>  {fields[h]} </li>"
        ul += "</ul>"
        return format_html(ul)
    except Exception as e:
        return f"{e}"


@register.simple_tag
def ListUlForMultipleQuerySet(request=None, searchable_names='', queryset=None):
    data_header =  searchable_names.split(',')
    ul = ""
    
    try:
        ul += "<ul class='list-group list-group-flush'>"
        res=request.META

        serialized_data =  serializers.serialize('python', queryset, use_natural_foreign_keys=True, use_natural_primary_keys=True) 
        for s in serialized_data:
            fields =  s.get('fields')
            for h in data_header:
                ul += f"<li class='list-group-item'><b>{str(h).replace('_',' ').title()}: </b>  {fields[h]} </li>"
        ul += "</ul>"
        return format_html(ul)
    except Exception as e:
        return f"{e}"



@register.simple_tag
def related_item(request=None, object=None, lookup_field=None, id=None, searchable_names=''):
    try:
        data =  {}
        ul = ""
        ul += "<ul class='list-group list-group-flush'>"
        data_header =  searchable_names.split(',')
        data[lookup_field] = id
        # objects
        obj = eval(object).objects.all().filter(**data)
        # 
        serialized_data =  serializers.serialize('python', obj, use_natural_foreign_keys=True, use_natural_primary_keys=True)

        for x in serialized_data:
            fields = x.get('fields')
            for h in data_header:
                ul += f"<li class='list-group-item'><b>{str(h).replace('_',' ').title()}: </b>  {fields[h]} </li>"
        ul += "</ul>"

        return format_html(ul)
    except Exception as e:
        return f"{e}"