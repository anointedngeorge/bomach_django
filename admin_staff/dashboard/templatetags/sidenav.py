from django import template
from django.core import serializers
from django.utils.html import format_html
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from ..app_list import APPLIST


register = template.Library()


@register.simple_tag
def sidenavigation(adminsite=''):
    html = ''
    for applist in APPLIST:
        icon =  applist.get('icon') if applist.get('icon') != '' else "fa fa-circle"
        html += f'<li>'
        if applist.get('has_model_dropdown'):
            html += f'''<a>
                    <i class="{applist.get('icon')}"></i>
                        {applist.get('heading')}
                        <span class="fa fa-chevron-down"></span>
                </a>'''
            html += '<ul class="nav child_menu">'
            for  model in applist.get('models'):
                html += f'<li> <a href="/{adminsite}/{ model.get("url")}">{model.get("title")}</a> </li>'
            html += '</ul>'
        else:
            html += f'''<a href="/{adminsite}/{applist.get('url', None)}" >
                    <i class="{applist.get('icon')}"></i>
                        {applist.get('heading')}
                    </a>'''
                
        html += '</li>'
    return mark_safe(html)


