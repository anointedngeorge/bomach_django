
from django.utils.html import format_html, html_safe
from plugins.query_builder import queryFormat
from plugins.permissions import checkCodenameInPermGroup

# can_perform_extra_action
def statusActions(data={}, status='pending', request=object):
    d = {
        'pending':[
            {'name':'Confirm','url':'confirm/', 'classname':'btn btn-sm btn-primary'}
        ],
        'query':{'id':1}
    }
    
    
    try:
        checkingroup = checkCodenameInPermGroup(
            group_name=request.user.roles,
            permission_codename='can_perform_extra_action'
        )
        query = queryFormat(param=data.get('query'))
        table = ''
        table += '<table>'
        table += "<tr>"
        check_data =  data.get(status)

        if check_data !=  None:
            for x in check_data:
                if checkingroup:
                    table += f"<td><a href='{x.get('url')}?{query}' class='{x.get('classname')}'>{x.get('name')}</a></td>"
        else:
            return []
        table += "</tr>"
        table += '</table>'
        return format_html(table)
    except:
        return 'No action specified yet'

