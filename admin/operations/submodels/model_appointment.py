from django.db import models
# from authuser.models import *
from django.utils import timezone
from plugins.dropdown import *




class Appointment(models.Model):
    STATUS_CHOICE = [
        ('pending','Pending'),
    ]
    code = models.CharField(max_length = 150, blank=True, null=True)
    status  = models.CharField(max_length = 150, default='pending', choices=STATUS_CHOICE, blank=True, null=True)
    name = models.CharField(max_length = 150, verbose_name='Client Name')
    email = models.EmailField(max_length=150, verbose_name='Client Email')
    phone = models.CharField(max_length = 150, verbose_name='client Phone')
    branch = models.ForeignKey(to="authuser.Branch", related_name='appointment_rel', 
    on_delete=models.CASCADE)
    designation = models.ForeignKey(to='human_resource.Designation', 
    on_delete=models.CASCADE, null=True, blank=True, related_name='appointment_designation')
    service_category = models.ForeignKey(to="settings.ServiceCategory", related_name='appointment_service_rel', 
    on_delete=models.CASCADE)
    message = models.TextField()
    # appointment_time = models.TimeField(auto_now=False,default='00:00:00')
    appointment_date  = models.DateTimeField(auto_now=False, default=timezone.datetime.now, unique=True)
    

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'


    def natural_key(self):
        return self.__str__()
    
    def action(self):
        modalname = self._meta.model.__name__
        action = {'pending': [
                    {"name":'Accept', "href":f"employee-profile", "is_button":False, 
                    "query":{'id':self.id}},
                     {"name":'Reject', "href":f"employee-profile", "is_button":False, 
                    "query":{'id':self.id}},
                ],
                'Rejected': [
                    {"name":'Reschedule', "href":f"employee-profile", "is_button":False, 
                    "query":{'id':self.id}},
                ],


                }


            
 
        return dictDropdown(
            action=action, 
            modelname=modalname,
            status=self.status,
            show_media=False,
            code=self.code
        )


    
   
    

    
    
    
    