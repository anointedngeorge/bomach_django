

import importlib
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
import os

from authuser.models.user import *
from dashboard.forms.custom_forms import vendorBusinessForm


# for view bussiness
def viewOtherVendorBusinesses(request, *args, **kwargs):
    http_referer =  request.META.get("HTTP_REFERER")
    context={}
    return TemplateResponse(request, f"admin/views/view_businesses.html", context=context)



# for riders
def viewRidersModelProfile(request, *args, **kwargs):
        http_referer =  request.META.get("HTTP_REFERER")
        context = {}
        context['title'] = f"Detail View Page "
        current_template = kwargs.get("current_template")
        rider_id = kwargs.get("id")
        # # 
        foundobj = Driver.objects.all().filter(id=rider_id)

        if foundobj.exists():
            foundobj = foundobj.get()
            context['contextdata'] = foundobj.getObjectData()
        return TemplateResponse(request, f'{current_template}/views/view_profile_details.html', 
                                context)

def viewAgentModelProfile(request, *args, **kwargs):
        http_referer =  request.META.get("HTTP_REFERER")
        context = {}
        context['title'] = f"Detail View Page "
        current_template = kwargs.get("current_template")
        agent_id = kwargs.get("id")
        # # 
        foundobj = Agent.objects.all().filter(id=agent_id)

        if foundobj.exists():
            foundobj = foundobj.get()
            context['contextdata'] = foundobj.getObjectData()
        return TemplateResponse(request, f'{current_template}/views/view_profile_details.html', context)


# def viewRidersBike(request, *args, **kwargs):
#     http_referer =  request.META.get("HTTP_REFERER")
#     context = {}
#     context['title'] = f" Bike "
#     current_template = kwargs.get("current_template")
#     agent_id = kwargs.get("id")
#     # # 
#     # foundobj = Agent.objects.all().filter(id=agent_id)
#     return render(request, f"admin/rider_bike.html", context=context)