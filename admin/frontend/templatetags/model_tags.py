from customer.models import *
import uuid
from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def show_customers(f=None):
    customer = Customer.objects.all()
    return customer



@register.simple_tag
def show_file_url(code=None):
    url = f"settings/gallery/"
    return url