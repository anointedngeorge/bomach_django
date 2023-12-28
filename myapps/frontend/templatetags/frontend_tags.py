from customer.models import *
import uuid
from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import os
from frontend.models.settings import DataJosn
from frontend.models import *



register = template.Library()

@register.simple_tag
def show_tags(tag=None):
    data =  DataJosn.objects.all().filter(tag=tag)
    return data



@register.simple_tag
def frontdata(model='', is_active=None, nindex=0):
    try:
        if isinstance(is_active, bool):
            data =  eval(model).objects.all().filter(
                is_active=is_active
            )
            return data[:nindex] if nindex > 0 else data
        data =  eval(model).objects.all()
        return data[:nindex] if nindex > 0 else data
    except Exception as e:
        return str(e)
    




