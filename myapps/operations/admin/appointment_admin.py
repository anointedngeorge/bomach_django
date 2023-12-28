from django.contrib import admin
from django.http import HttpResponse,JsonResponse
from operations.models import *
from operations.forms import *
import uuid
from actions.appointment_action import *
from django.urls import path, include
from typing import List



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone','branch','designation','appointment_date','status','action']
    form = AppointmentForm
    actions = [ViewAppointmentProfile]

    def get_urls(self):
        url = super().get_urls()
        url_add = [
            path('appointment-status/<int:appoint_id>/<str:status>', self.appointment_status, name='appointment-status')
        ]
        return url_add + url

    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        coded = f"{uuid.uuid4().hex}"
        obj.code = coded
        obj.save()
        return super().response_add(request, obj, post_url_continue)

    def appointment_status(self, request, appoint_id=None, status=None):
        data = {'message':'', 'status':False}
        try:
            md = self.model.objects.all().filter(id=appoint_id)
            if status != 'message':
                md.update(**{'status':status})
                data['status'] = True
                data['message'] = 'Successful'

            else:
                pass
            return JsonResponse(data)
        except Exception as e :
            data['message'] = 'Failed'
            data['status'] = False
            print(e)
        return JsonResponse(data)


    class Media:
        js = (
            # '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'custom/jquery-3.6.4.min.js', # jquery
            'custom/app.js',       # project static folder
        )

