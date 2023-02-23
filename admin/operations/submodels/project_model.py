from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.

from human_resource.models import *
from human_resource.submodels.departments import Department
from customer.models import Customer


class OperationProject(models.Model):
    project_id = models.CharField(max_length = 150, null=True, blank=True)
    project_name = models.CharField(max_length = 150, null=True, blank=True)
    start_date = models.DateField(auto_now=False, default='2023-03-02')
    expected_end_date = models.DateField(verbose_name='end date(deadline)', auto_now=False, default='2023-03-02')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, 
    null=True, related_name='project_department')
    project_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    budget = models.CharField(max_length = 150, null=True, verbose_name="budget(N)")
    hour_estimated = models.TimeField(auto_now=False, default='00:00:00', null=True)
    project_desciption = models.TextField(null=True)
    project_owner = models.CharField(
        max_length = 150, null=True, help_text='Please Enter Unique Id.'
        )
    created_at = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
    
    def __str__(self) -> str:
        return self.project_name
    
    