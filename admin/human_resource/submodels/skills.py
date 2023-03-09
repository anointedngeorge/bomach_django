from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.
from human_resource.models import *

class Skill(models.Model):
    code = models.CharField(max_length = 150, null=True)
    name = models.CharField(max_length = 150)
    description = models.TextField(default='----')
    designation = models.ForeignKey(to='human_resource.Designation', on_delete=models.CASCADE, null=True)
    
    # employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True,
    #  related_name="hr_skills_employee_relationship")
    # department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True,
    #  related_name="hr_skills_department_relationship")
    created_at = models.DateField(auto_now=True)
    

    def __str__(self) -> str:
        return self.name