

from django.http import HttpResponse
from django.shortcuts import redirect, render
import os
from django.contrib import messages as msg

from authuser.models.user import *
from dashboard.forms.custom_forms import vendorBusinessForm


def addOtherVendorBusinesses(request, *args, **kwargs):
    http_referer =  request.META.get("HTTP_REFERER") # for proper redirection
    context={}
    current_template = kwargs.get("current_template")
    if request.method == "POST":

        f =  vendorBusinessForm(request.POST, request.FILES)
        f.save()
        # VendorOtherBusiness.objects.all().create()
        return redirect(http_referer)
    # get
    vendor_id = kwargs.get('id', None)
    vend = Vendor.objects.all().filter(id=vendor_id).get()
    
    context['form'] = vendorBusinessForm
    context['name'] = f"{vend.first_name} {vend.last_name}"
    context['vendor_id'] = vendor_id
    return render(request, f"{current_template}/add/add_businesses.html", context=context)



def EmergencyDetailsFun(request, *args, **kwargs):
            http_referer =  request.META.get("HTTP_REFERER") # for proper redirection
            id = kwargs.get("id", None)
            current_template = kwargs.get("current_template", 'admin')
            name = "Emergency Details"
            context = {}
            context['title'] = f"{str(name).title()} "
            context['site_header'] = f"Edit {name}"
            context['site_title'] = f"m"
            context['register_url'] = f'add/{id}/EmergencyDetailsFun/'
            context['adminsite'] = 'superadmin'
            # if name == 'emergency':
            from authuser.forms.user_form import (
                EmergencyContactDetailsForm, 
                EmergencyContactDetails,
            )
            FORM = EmergencyContactDetailsForm
            emergency = EmergencyContactDetails.objects.filter(user_id=id)
            if emergency.exists():
                context['form'] = FORM(instance=emergency.first())
                if request.method == "POST":
                    f=FORM(request.POST, instance=emergency.first())
                    if f.is_valid():
                        f.save()
                        msg.success(request, "Profile Updated")
                        return redirect(http_referer)
            else:
                 context['form'] = FORM()
                 if request.method == "POST":
                    f=FORM(request.POST, user_id=id)
                    if f.is_valid():
                        f.save()
                        return redirect(http_referer)
           
            return render(request, f'{current_template}/add/complete_registration.html', context)



def AcademicDetailsFun(request, *args, **kwargs):
            http_referer =  request.META.get("HTTP_REFERER") # for proper redirection
            id = kwargs.get("id", None)
            current_template = kwargs.get("current_template", 'admin')
            name = "Academic Details"
            context = {}
            context['title'] = f"{str(name).title()} "
            context['site_header'] = f"Edit {name}"
            context['site_title'] = f"m"
            context['register_url'] = f'add/{id}/AcademicDetailsFun/'
            context['adminsite'] = 'superadmin'
           
            # if name == 'emergency':
            from authuser.forms.user_form import (
                AcademicDetailsForm,
                AcademicDetails,
                EmploymentDetailsForm,
                MedicalDetailsForm
            )

            FORM = AcademicDetailsForm

            emergency = AcademicDetails.objects.filter(user_id=id)
            if emergency.exists():
                context['form'] = FORM(instance=emergency.first())
    
                if request.method == "POST":
                    f=FORM(request.POST, instance=emergency.first())
                    if f.is_valid():
                        f.save()
                        msg.success(request, "Academic Profile Updated")
                        return redirect(http_referer)
            else:
                 context['form'] = FORM()

                 if request.method == "POST":
                    f=FORM(request.POST, user_id=id)
                    if f.is_valid():
                        f.save()
                        msg.success(request, "Academic profile added")
                        return redirect(http_referer)
           
            return render(request, f'{current_template}/add/complete_registration.html', context)


def MedicalDetailsFun(request, *args, **kwargs):
            http_referer =  request.META.get("HTTP_REFERER") # for proper redirection
            id = kwargs.get("id", None)
            current_template = kwargs.get("current_template", 'admin')
            name = "Medical Details"
            context = {}
            context['title'] = f"{str(name).title()} "
            context['site_header'] = f"Edit {name}"
            context['site_title'] = f"m"
            context['register_url'] = f'add/{id}/MedicalDetailsFun/'
            context['adminsite'] = 'superadmin'
           
            # if name == 'emergency':
            from authuser.forms.user_form import (
                EmploymentDetailsForm,
                MedicalDetailsForm,
                MedicalDetails
            )

            FORM = MedicalDetailsForm

            emergency = MedicalDetails.objects.filter(user_id=id)
            if emergency.exists():
                context['form'] = FORM(instance=emergency.first())
    
                if request.method == "POST":
                    f=FORM(request.POST, instance=emergency.first())
                    if f.is_valid():
                        f.save()
                        msg.success(request, "Medical Profile Updated")
                        return redirect(http_referer)
            else:
                 context['form'] = FORM()

                 if request.method == "POST":
                    f=FORM(request.POST, user_id=id)
                    if f.is_valid():
                        f.save()
                        msg.success(request, "Medical profile added")
                        return redirect(http_referer)
           
            return render(request, f'{current_template}/add/complete_registration.html', context)



def EmploymentDetailsFun(request, *args, **kwargs):
            http_referer =  request.META.get("HTTP_REFERER") # for proper redirection
            id = kwargs.get("id", None)
            current_template = kwargs.get("current_template", 'admin')
            name = "Employment Details"
            context = {}
            context['title'] = f"{str(name).title()} "
            context['site_header'] = f"Edit {name}"
            context['site_title'] = f"m"
            context['register_url'] = f'add/{id}/EmploymentDetailsFun/'
            context['adminsite'] = 'superadmin'
           
            # if name == 'emergency':
            from authuser.forms.user_form import (
                EmploymentDetailsForm,
                EmploymentDetails
            )

            FORM = EmploymentDetailsForm

            emergency = EmploymentDetails.objects.filter(user_id=id)
            if emergency.exists():
                context['form'] = FORM(instance=emergency.first())
    
                if request.method == "POST":
                    f=FORM(request.POST, instance=emergency.first())
                    if f.is_valid():
                        f.save()
                        msg.success(request, "Employment Profile Updated")
                        return redirect(http_referer)
            else:
                 context['form'] = FORM()

                 if request.method == "POST":
                    f=FORM(request.POST, user_id=id)
                    if f.is_valid():
                        f.save()
                        msg.success(request, "Employment profile added")
                        return redirect(http_referer)
           
            return render(request, f'{current_template}/add/complete_registration.html', context)



def AssignRiderToAgent(request, *args, **kwargs):
        from authuser.forms import AgentRider, VendorRiderForm
        http_referer =  request.META.get("HTTP_REFERER") # for proper redirection
        current_template = kwargs.get("current_template", 'admin')
        context = {}
        id =  kwargs.get('id')
        context['title'] = f"Assign Agent to vendor"
        context['site_header'] = f"Assigned"
        context['site_title'] = f"m"
        context['register_url'] = f'add/{id}/AssignRiderToAgent/'
        context['adminsite'] = "superadmin"
        CURRENT_TEMPLATE = 'superadmin'
        
        FORM = VendorRiderForm
        emergency = AgentRider.objects.filter(agent_id=id)
        if emergency.exists():
            context['form'] = FORM(instance=emergency.first())

            if request.method == "POST":
                f=FORM(request.POST, instance=emergency.first())
                if f.is_valid():
                    f.save()
                    msg.success(request, "Updated...")
                    return redirect(http_referer)
        else:
            context['form'] = FORM()

            if request.method == "POST":
                f=FORM(request.POST)
                if f.is_valid():
                    f.save()
                    msg.success(request, "Assigned...")
                    return redirect(http_referer)
        
        return render(request, f'{current_template}/add/assign_bike.html', context)


def AssignVendorToAgent(request, *args, **kwargs):
        from authuser.forms import VendorAgentForm, AgentRider
        http_referer =  request.META.get("HTTP_REFERER") # for proper redirection
        current_template = kwargs.get("current_template", 'admin')
        context = {}
        id =  kwargs.get('id')
        context['title'] = f"Assign Agent to vendor"
        context['site_header'] = f"Assigned"
        context['site_title'] = f"m"
        context['register_url'] = f'add/{id}/AssignVendorToAgent'
        context['adminsite'] = "superadmin"
        CURRENT_TEMPLATE = 'superadmin'
        
        FORM = VendorAgentForm
        emergency = AgentVendor.objects.filter(agent_id=id)
        if emergency.exists():
            context['form'] = FORM(instance=emergency.first(), userid=id)

            if request.method == "POST":
                f=FORM(request.POST, instance=emergency.first(), userid=id)
                if f.is_valid():
                    f.save()
                    msg.success(request, "Updated...")
                    return redirect(http_referer)
        else:
            context['form'] = FORM(userid=id)

            if request.method == "POST":
                f=FORM(request.POST)
                if f.is_valid():
                    f.save()
                    msg.success(request, "Assigned...")
                    return redirect(http_referer)
    
        return render(request, f'{current_template}/add/assign_bike.html', context)



def RiderBike(request, *args, **kwargs):
        from assetsAndEquipment.forms.assets_form import AssignedBikeForms, AssignMotocycleToRider
        http_referer =  request.META.get("HTTP_REFERER") # for proper redirection
        current_template = kwargs.get("current_template", 'admin')
        context = {}
        id =  kwargs.get('id')
        user =  Driver.objects.filter(id=id).get()
        context['full_name'] = f"{user.first_name} {user.last_name}"
        context['title'] = f"{user.first_name} {user.last_name} Bike Assignment"
        context['site_header'] = f"Assigned"
        context['site_title'] = f"m"
        context['register_url'] = f'add/{id}/RiderBike/'
        context['adminsite'] = "superadmin"
        CURRENT_TEMPLATE = 'superadmin'

        asset_item =  AssignMotocycleToRider.objects.all()

        if asset_item.filter(user_id=id).exists():
           item = asset_item.filter(user_id=id)
           context['items'] =  item
        
        FORM = AssignedBikeForms
        
        if request.method == "POST":
            # f=FORM(request.POST)
            data = request.POST.dict()
            data.pop('csrfmiddlewaretoken')
            
            data_formatted = {
                 'user_id':data.get('user'),
                 'motocycle_id':data.get('motocycle')
            }
            
            asset_item.get_or_create(**data_formatted)

            # if f.is_valid():
            #     f.save()
            msg.success(request, "Successful...")
            return redirect(http_referer)

        context['form'] = FORM(userid=id)
        return render(request, f'{current_template}/add/rider_bike.html', context)

        
