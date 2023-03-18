from django.db import models
# from authuser.models import *
from django.utils import timezone
from plugins.dropdown import *


class Appointment(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length = 150)
    branch = models.ForeignKey(to="authuser.Branch", related_name='appointment_rel', 
    on_delete=models.CASCADE)
    service_category = models.ForeignKey(to="settings.ServiceCategory", related_name='appointment_service_rel', 
    on_delete=models.CASCADE)
    message = models.TextField()
    appointment_time = models.TimeField(auto_now=False,default='00:00:00')
    appointment_date = models.DateField(auto_now=False, default=timezone.now)
    
    
    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    
   
    

    
    
    
    