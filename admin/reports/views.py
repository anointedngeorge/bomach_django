from django.shortcuts import render
import os
from http import HTTPStatus
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.


def getReport(request, template_name, model):
    context =  {}
    filename = f"report_{template_name}.html".lower()
    # /home/eit/DjangoProjects/bomach_django/admin/templates/reports/contract
    _template =  os.path.realpath(f"templates/reports/{template_name}")
    if os.path.exists(_template):
        _template_file =  os.path.realpath(f"templates/reports/{template_name}/{filename}")
        if os.path.exists(_template_file):
            return render(request, f"{_template}/{filename}", context=context)
        else:
            with open(_template_file, 'w') as f:
                pass
            
            messages.add_message(request, messages.INFO, '.')
            return redirect("/admin")
            # return HttpResponse(f"We created this file {filename}. You can reload to continue. <a href='/admin'>Reload</a>.")
    else: 
        os.mkdir(os.path.realpath(f"templates/reports/{template_name}"))
        return redirect("/admin")
        # return HttpResponse(f"Path to folder with the name  {template_name}, not found. <a href='/admin'>Back To Admin</a>")