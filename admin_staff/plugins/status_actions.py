
from django.utils.html import format_html, html_safe
from plugins.query_builder import queryFormat
from plugins.permissions import checkCodenameInPermGroup
import json
from plugins.generator import generator


# can_perform_extra_action
def statusActions(data={}, status='pending', request=object, type='btn'):
    # d = {
    #     'pending':[
    #         {'name':'Confirm','url':'confirm/', 'status':'' ,'classname':'btn btn-sm btn-primary'}
    #     ],
    #     'query':{'id':1}
    # }
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
                code = generator(6)
                status =  x.get('status')
                function =  x.get('function')
                if checkingroup:
                    if type == 'btn':
                        # table += "<form>"
                        table += f"<td><button data-message='{status}' data-function='{function}' type='button' class='{x.get('classname')} status-button' id='{code}'>{x.get('name')}</button></td>"
                        # table += "</form>"
                    elif type == 'anchor':
                        table += f"<td><a href='{x.get('url')}?{query}' class='{x.get('classname')}'>{x.get('name')}</a></td>"
                    else:
                        table += 'Choose btw btn:submit | <a href></a>'
        else:     
            return '-'
        
        # print(status)
        table += "</tr>"
        table += '</table>'
        return format_html(table)
    except:
        return 'No action specified yet'

