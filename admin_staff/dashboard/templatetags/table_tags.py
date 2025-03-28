from django import template
from django.core import serializers
from django.utils.html import format_html
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

from operator import methodcaller

register = template.Library()

table_th_attributes = {
    "class":"sorting_asc",
    "tabindex":"0",
    "aria-controls":"datatable-buttons",
    "rowspan":"1",
    "colspan":"1",
    "style":"width: 90px;",
    "aria-sort":"ascending",
    "aria-label":"Name: activate to sort column descending",
}


table_td_attributes = {
    "role":"row",
    "class":"even",
}


def tableClassAtrrs(data={}):
    return ' '.join([f'{key}="{value}"' for key, value in data.items()])






def table_head(object, **kwargs):
    heads =  object.list_display
    attributes = tableClassAtrrs(table_th_attributes)
    table = ""
    table += "<thead>"
    table += "<tr>"
    clss = 'text-uppercase text-secondary text-xxs font-weight-bolder opacity-7'
    # table += f"<th data-sortable='true' style='width: 9.25925925925926%'>#</th>"
    # table += f"<th class='{clss}'  data-sortable='false' style='width: 9.25925925925926%'><input type='checkbox'  name='delete_checkbox_main' class='delete_checkbox_main'  id='delete_checkbox_main' /></th>"
    for head in heads:
        table += f"<th {attributes}>{str(head).replace('_', ' ').upper()}</th>"
    table += f"<th {attributes}>Remove</th>"
    table += "</tr>"
    table += "</thead>"
    return table


def table_body(object=None, request=None):
    try:
        # print(object.model_admin.trackFunction)
        heads =  object.list_display
        list_display_links =  object.list_display_links
        attributes = tableClassAtrrs(table_th_attributes)
        table = ""
       
        counter = 0
        index_counter =  1
        table += "<tbody>"
        for tbody in object.result_list:
            even_odd =  "even" if (counter % 2 == 0)  else "odd"
            pk = eval("tbody.pk")
            table += f"<tr data-index='{counter}' {attributes} class='{even_odd}'>"
            # table += f"<td>{index_counter}</td>"
            # table += f"<td><input type='checkbox' name='delete_checkbox' value='{pk}' class='delete_checkbox'  id='delete_checkbox_{index_counter}' /></td>"
            for head in heads:
                table += f"<td>"
                # print(hasattr(eval(f"object.model"), head), head)
                # include a function call from either model or admin
                if hasattr(eval(f"object.model"), head) and callable(getattr(object.model, head)):
                   
                    # this will check if the attribute of the class is callable
                    method = getattr(object.model, head)
                    data = methodcaller(method.__name__)(tbody)  # Call the method with 'tbody' as the 'self' argument
                    table += f"{data}"
                
                else: 
                    if head in list_display_links:
                    # check if it is a function
                        data = eval(f"tbody.{head}")
                        table += f"<a href='{pk}/change' class='text text-primary'> {data}  </a>"
                    else: 
                        data = eval(f"tbody.{head}")
                        table += f"{data}"
                    table += "</td>"
            table += f"<td><a href='{tbody.pk}/delete' class='link' >Delete</a></td>"
            table += "</tr>"
            counter += 1
            index_counter += 1
        table += "</tbody>"
        return table
    
    except Exception as e:
        return str(e)


@register.simple_tag
def change_list_table(object=None, request=None):

    table = ""
    if object == None:
        return None
    table +=  table_head(object=object)
    table +=  table_body(object=object, request=request)

    return format_html(table)


@register.simple_tag
def ObjectView(object=None, fields='id,'):
    try:
        fields =  fields.split(',')
     
        table = ""
        if object:
            for key in fields:
                if key != "":
                    data = eval(f"object.{key}")
                    table += "<tr>"
                    table += f"<td>{str(key).replace('_', ' ').upper()}: </td>"
                    table += f"<td>{data}</td>"
                    table += "</tr>"
            return format_html(table)
        return ''
    except Exception as e:
        return str(e)
    


@register.simple_tag
def ObjectViewArray(object=None, fields='id,'):
    try:
        fields =  fields.split(',')
        table = ""

        if object:
            table += "<thead>"
            table += "<tr>"
            for key in fields:
                    if key != "":
                        table += f"<td>{str(key).replace(',',' ').title()}</td>"
            table += "</tr>"
            table += "</thead>"

            table += "<tbody>"
            
            for x in object:
                table += "<tr>"
                for key in fields:
                    if key != "":
                        data = eval(f"x.{key}")
                        table += f"<td>{data}</td>"
                table += "</tr>"

            table += "<tbody>"
            return format_html(table)
        return ''
    
    except Exception as e:
        return str(e)
    

@register.simple_tag
def MappingUiList(object=None, classname='ul'):
    ul = ""
    ul += f"<ul class='{classname}'>"
    dict_data = dict(object).items()
    for key, val in dict_data:
        formatted_heading = str(key).replace("_"," ").upper()
        ul += f"<li><h4>{formatted_heading}</h4></li>"
        
        value_data = val.items()
        for x , y in value_data:
            # print(x, y)
            ul += f"<li><b>{str(x).replace('_',' ').capitalize()}:</b> {str(y).capitalize()}</li>"
        ul += f"<br>"
    ul += "</ul>"
    return format_html(ul)