from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.
from human_resource.models import *
from authuser.submodels.branch_model import Branch
from human_resource.submodels.employee import Employee
import uuid




class Jobs(models.Model):
    code = models.CharField(max_length = 150, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    name  = models.CharField(max_length = 150, null=True)
    
    description = models.TextField()
   
    class Meta:
        verbose_name = 'Job Role'
        verbose_name_plural = 'Job Roles'
    
    def __str__(self) -> str:
        return f"{self.branch} - {self.employee}"


class Job_history(models.Model):
    code = models.CharField(max_length = 150, null=True)
    jobs = models.ForeignKey(Jobs, on_delete=models.CASCADE, null=True, blank=True,
     related_name="hr_jobs_relationship")
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True,
     related_name="hr_jobs_employee_relationship")
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True,
     related_name="hr_department_relationship")
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=True)

    

    class Meta:
        verbose_name = 'Job History'
        verbose_name_plural = 'Job Histories'

    def __str__(self) -> str:
        res = self.jobs if self.jobs is not None else 'Job histories created.'
        return res

    
    