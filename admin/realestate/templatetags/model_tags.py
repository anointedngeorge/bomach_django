from customer.models import *
from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.conf import settings

register = template.Library()

path = settings.ADMIN_URI
# @register.inclusion_tag('templateResponse/sell_plot.html')

@register.simple_tag
def show_customers(f=None, name='', classname=''):
    customer = Customer.objects.all()
    html = ""
    html += f"<select name={name} class={classname}>"
    for x in customer:
        html += f"<option value={x.id}>{x.name}</option>"
    html += "</select>"
    return format_html(html)



@register.simple_tag
def show_status(name='', classname=''):
    status = [
        ("pending","Pending"),
        ("sold","Sold"),
        ("reserve","Reserve"),
    ]
    html = ""
    html += f"<select id='status_container_select' name={name} class={classname}>"
    for x in status:
        html += f"<option value={x[0]}>{x[1]}</option>"
    html += "</select>"
    return format_html(html)


@register.simple_tag
def show_code(f=None):
    uid = str(uuid.uuid4()).replace("-", "")[:20]
    return uid


@register.simple_tag
def show_path(f=None):
    return path