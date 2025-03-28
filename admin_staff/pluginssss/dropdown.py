from django.utils.html import format_html
from django.urls import reverse_lazy

from plugins.url import (
    local_file_url_image,
    api_fetch_image
)

from plugins.query_builder import queryFormat


REPORT_LINK = '/admin/reports/get-reports'






def dictDropdown(action=[], link='', status='', modelname='', code='', report_title='',  report_template_name='', is_report=False, show_media=False):
        """
        This is a dropdown menue
        """
        html = ""
    
        try:
            # get the status that match in the action object
            get_status =  None
            if not action.get(status) == None:
                get_status =  action.get(status)
            else:
                get_status = []
                
            html += "<div class='table table-responsive'>"
            html += "<table class='table table-sm table-condensed'>"
            html += "<tr>"
            query = ''
            for x in get_status:
                query = queryFormat(x.get('query')) if x.get('query') != None else ''
                if x.get('is_button'):
                    html += f"<td><button type='button' data-url='{x.get('href')}' value='{query}'>{str(x.get('name')).title()}</button></td>"
                else:
                    html += f"<td><a  href='{x.get('href')}?{query}'>{str(x.get('name')).title()}</a></td>"
            if show_media:
                html += f"<td><a  href='{local_file_url_image(code)}?model={modelname}'>Upload File(s)</a></td>"
                html += f"<td><a  href='{api_fetch_image(code)}?model={modelname}' target='_blank'>Get Files</a></td>"
            if is_report:
                html += f"<td><a  href='{link}/{report_template_name}/{modelname}/?{query}'>{report_title.title()}</a></td>"

            html += "</tr>"
            html += "</table>"
            html += "</div>"

            return format_html(html)
        except Exception as e:
            return (e)


def singleDropdown(action=[], modelname='', link='', code='', report_title='', report_template_name='task', is_report=False, show_media=False):
        try:
            html = ""
            # get the status that match in the action object
            html += "<div class='table table-responsive'>"
            html += "<table class='table table-sm table-condensed'>"
            html += "<tr>"
            query = ''
            for x in action:
                query = queryFormat(x.get('query')) if x.get('query') != None else ''
                if x.get('is_button'):
                    html += f"<td><button  data-url='{x.get('href')}' value='{query}'>{x.get('name')}</button></td>"
                else:
                    html += f"<td><a href='{x.get('href')}?{query}'>{x.get('name')}</a></td>"
            
            if show_media:
                html += f"<td><a  href='{local_file_url_image(code)}?model={modelname}'>Upload File(s)</a></td>"
                html += f"<td><a  href='{api_fetch_image(code)}?model={modelname}' target='_blank'>Get Files</a></td>"
            
            if is_report:
                html += f"<td><a  href='{link}/{report_template_name}/{modelname}/?{query}'>{report_title.title()}</a></td>"
            
            html += "</tr>"
            html += "</table>"
            html += "</div>"

            return format_html(html)
        except:
            pass