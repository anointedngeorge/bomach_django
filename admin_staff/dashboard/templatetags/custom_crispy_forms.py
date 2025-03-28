from django import template
from django.core import serializers
from django.utils.html import format_html
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

from plugins.word_transform import is_camel_or_pascal_case




register = template.Library()


@register.filter
def render_form2(form):
    html = '<div class="row mt-4 mb-4">'
    for field in form:
        html += "<div class='col-sm-2 mt-4'>"
        html += f"<label> {is_camel_or_pascal_case(field.label)} </label>"
        if field.field.required:
            html += " <span class='required-tag text text-danger'>*</span>"
        html += f" {field} "
        html += f" {field.errors} "
        html += "</div>"
    html += '</div>'
    return mark_safe(html)



@register.filter
def render_form3(form):
    html = '<div class="row mt-4 mb-4">'
    for field in form:
        html += "<div class='col-sm-3 mt-4'>"
        html += f"<label> {is_camel_or_pascal_case(field.label)} </label>"
        if field.field.required:
            html += " <span class='required-tag text text-danger'>*</span>"
        html += f" {field} "
        html += f" {field.errors} "
        html += "</div>"
    html += '</div>'
    return mark_safe(html)




@register.filter
def render_form4(form):
    html = '<div class="row mt-4 mb-4">'
    for field in form:
        html += "<div class='col-sm-4 mt-4'>"
        html += f"<label> {is_camel_or_pascal_case(field.label)} </label>"
        if field.field.required:
            html += " <span class='required-tag text text-danger'>*</span>"
        html += f" {field} "
        html += f"{field.errors}"
        html += "</div>"
    html += '</div>'
    return mark_safe(html)