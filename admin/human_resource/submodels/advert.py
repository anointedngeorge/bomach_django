from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.
from human_resource.models import *

class Advert(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
     related_name="hr_advert_user_relationship")
    name = models.CharField(max_length = 150)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True,
     related_name="hr_advert_department_relationship")
    job_position= models.ForeignKey('Jobs', on_delete=models.CASCADE, null=True, blank=True,
     related_name="hr_advert_position_relationship")
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    description = models.TextField()
    is_hired = models.BooleanField(default=False)
    is_still_open = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Advert'
        verbose_name_plural = 'Job Advert'
    
    
    def __str__(self) -> str:
        return self.name
    
    