from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.
from human_resource.models import *

class Jobs(models.Model):
    job_title = models.CharField(max_length = 150)
    description = models.TextField()
    min_salary = models.CharField(max_length = 150)
    max_salary = models.CharField(max_length = 150)

    

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
    
    def __str__(self) -> str:
        return self.job_title


class Job_history(models.Model):
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

    
    