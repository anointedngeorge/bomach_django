from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.
from human_resource.models import *


class Salary(models.Model):
    code = models.CharField(max_length = 150, null=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE,
     related_name="hr_jobs_salary_relationship")
    amount = models.CharField(max_length = 150)
    reduction = models.CharField(max_length = 150)
    paid_date = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Salaries'
        verbose_name_plural = 'Salary'
    
    def __str__(self) -> str:
        return self.amount