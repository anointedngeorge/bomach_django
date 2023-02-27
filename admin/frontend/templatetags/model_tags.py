from customer.models import *
import uuid
from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import os



register = template.Library()

@register.simple_tag
def show_customers(f=None):
    customer = Customer.objects.all()
    return customer



@register.simple_tag
def show_file_url(code=None):
    url = f"settings/gallery/"
    return url


@register.simple_tag
def loadSystemSettingFile(code=None):
    filepath =  os.path.realpath("/system.json")
    if os.path.exists(filepath):
        print('Yes')
        return filepath
    return {}