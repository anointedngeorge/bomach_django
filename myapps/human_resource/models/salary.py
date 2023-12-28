from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.
from human_resource.models import *
from authuser.models.branch_model import Branch
from djmoney.models.fields import MoneyField

class Salary(models.Model):
    code = models.CharField(max_length = 150, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='employee',  on_delete=models.CASCADE, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE,
     related_name="hr_jobs_salary_relationship")
    amount = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    reduction = models.CharField(max_length = 150, default=0, blank=True, null=True)
    paid_date = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Salaries'
        verbose_name_plural = 'Salary'
    
    def __str__(self) -> str:
        return f"{self.amount}"