from django.contrib import admin
from human_resource.models import *


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone','branch']
