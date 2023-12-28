

import importlib
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
import os

from authuser.models.user import *
from dashboard.forms.custom_forms import vendorBusinessForm


# for view bussiness
def viewRidersTask(request, *args, **kwargs):
    context = {}
    context['title'] = f"Detail View Page "
    current_template = kwargs.get("current_template")
    rider_id = int(kwargs.get("id"))
    
    # # 
    foundobj = Driver.objects.all().filter(id=rider_id)
    
    if foundobj.exists():
        foundobj = foundobj.get()
        context['contextdata'] = foundobj.getObjectData()

    return TemplateResponse(request, f"admin/tasks/view_riders_task.html", context=context)

