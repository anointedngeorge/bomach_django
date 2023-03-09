from django.shortcuts import render
import os
from http import HTTPStatus
from django.http import HttpResponse

# Create your views here.


def getReport(request, template_name, model, filename=None):
    context =  {}
    # /home/eit/DjangoProjects/bomach_django/admin/templates/reports/contract
    _template =  os.path.realpath(f"templates/reports/{template_name}")
    if os.path.exists(_template):
        return render(request, f"{_template}", context=context)
    else: 
        return HttpResponse(f"Path to folder with the name  {template_name}, not found. <a href='/admin'>Back To Admin</a>")