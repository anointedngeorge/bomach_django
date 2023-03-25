from django.contrib import admin
from django.http import HttpResponse
from operations.models import *
from operations.forms import *
import uuid

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone','branch','designation','appointment_date','status','action']
    form = AppointmentForm

    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        coded = f"{uuid.uuid4().hex}"
        obj.code = coded
        obj.save()
        return super().response_add(request, obj, post_url_continue)

    class Media:
        js = (
            # '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'custom/jquery-3.6.4.min.js', # jquery
            'custom/app.js',       # project static folder
        )

