from django.utils.html import format_html
from django.urls import reverse_lazy

from plugins.url import (
    local_file_url_image,
    api_fetch_image
)



def queryFormat(param={}):
    if len(param) > 0:
        str =  ""
        for x in param:
            str += f"{x}={param.get(x)}&"
            filtered =  str.rstrip('&')
        return filtered
    else:
        return ''

def dictDropdown(action=[], status='', modelname='', code=''):
        """
        This is a dropdown menue
        """
        html = ""
        # get the status that match in the action object
        get_status =  action.get(status)
        html += "<div class='table table-responsive'>"
        html += "<table class='table table-sm table-condensed'>"
        html += "<tr>"
        for x in get_status:
            query = queryFormat(x.get('query'))
            if x.get('is_button'):
                html += f"<td><button type='button' data-url='{x.get('href')}' value='{query}'>{str(x.get('name')).title()}</button></td>"
            else:
                html += f"<td><a  href='{x.get('href')}?{query}'>{str(x.get('name')).title()}</a></td>"
        html += f"<td><a  href='{local_file_url_image(code)}?model={modelname}'>Upload File(s)</a></td>"
        html += f"<td><a  href='{api_fetch_image(code)}?model={modelname}' target='_blank'>Get Files</a></td>"
        html += "</tr>"
        html += "</table>"
        html += "</div>"

        return format_html(html)


def singleDropdown(action=[], modelname='', code=''):
        html = ""
        # get the status that match in the action object
        html += "<div class='table table-responsive'>"
        html += "<table class='table table-sm table-condensed'>"
        html += "<tr>"
        for x in action:
            query = queryFormat(x.get('query'))
            if x.get('is_button'):
                html += f"<td><button  data-url='{x.get('href')}' value='{query}'>{x.get('name')}</button></td>"
            else:
                html += f"<td><a href='{x.get('href')}?{query}'>{x.get('name')}</a></td>"
        html += f"<td><a  href='{local_file_url_image(code)}?model={modelname}'>Upload File(s)</a></td>"
        html += f"<td><a  href='{api_fetch_image(code)}?model={modelname}' target='_blank'>Get Files</a></td>"
        html += "</tr>"
        html += "</table>"
        html += "</div>"

        return format_html(html)