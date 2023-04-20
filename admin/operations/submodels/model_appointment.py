from django.db import models
# from authuser.models import *
from django.utils import timezone
from plugins.dropdown import *




class Appointment(models.Model):
    STATUS_CHOICE = [
        ('pending','Pending'),
    ]
    user = models.ForeignKey(to='authuser.User', on_delete=models.CASCADE, 
    related_name='appointment_user_rel', null=True)
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
    start_date = models.TimeField(auto_now=False, default=timezone.datetime.now)
    end_date = models.TimeField(auto_now=False, default=timezone.datetime.now)
    message = models.TextField()
    # appointment_time = models.TimeField(auto_now=False,default='00:00:00')
    appointment_date  = models.DateTimeField(auto_now=False, default=timezone.datetime.now, unique=True)
    
    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
        permissions = (
            ("can_view_appointment_details", "can view appointment details"),
            ("can_perform_extra_action", "Can perform extra action"),
        )

    def get_profile(self):
        return f"{self.name}"
    
    def page_title(self):
        return f"{self.name}|{self.start_date}-{self.end_date}"

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


    
   
    

    
    
    
    