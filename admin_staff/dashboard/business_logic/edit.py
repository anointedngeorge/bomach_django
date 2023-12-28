

from django.shortcuts import redirect, render
import os

from authuser.models.user import *
from dashboard.forms.custom_forms import vendorBusinessForm



def editOtherVendorBusinesses(request, *args, **kwargs):
    http_referer =  request.META.get("HTTP_REFERER") # for proper redirection
    id = kwargs.get("id", 'admin')
    current_template = kwargs.get("current_template", 'admin')
    context={}
    return render(request, f"admin/add/edit_businesses.html", context=context)

# end of view business