from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.

from human_resource.models import *
from customer.models import Customer
from settings.submodels.model_service import ServiceCategory
from operations.submodels.project_model import OperationProject
from operations.submodels.site_model import OperationSite
from django_countries.fields import CountryField



class OperationContract(models.Model):
    code = models.CharField(max_length = 150, null=True)
    contract_title = models.CharField(max_length = 150, null=True, blank=True)
    contract_dependency = models.ForeignKey('OperationContract',blank=True, null=True, 
    on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=False, default='2023-03-02')
    expected_end_date = models.DateField(verbose_name='end date(deadline)', 
    auto_now=False, default='2023-03-02')
    contract_project  = models.ForeignKey(OperationProject, on_delete=models.CASCADE, null=True, blank=True)
    contract_site  = models.ForeignKey(OperationSite, on_delete=models.CASCADE, null=True, blank=True)
    contract_description = models.TextField(verbose_name='Project Scope Description', null=True)
    contract_type = models.CharField(max_length = 150, null=True)
    contract_value = models.IntegerField(blank=True, null=True)
    fullname = models.CharField(max_length = 150, null=True, verbose_name='fullname or cooperate name')
    contractor_phone = models.CharField(max_length = 150, null=True)
    address = models.CharField(max_length = 150, null=True)
    alternative_address = models.CharField(max_length = 150, null=True)
    country = CountryField(blank_label="(select country)", default='---',max_length=250)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length = 150, choices=[
        ('completed','Completed'),
        ('rejected','Rejected'),
        ('pending','Pending')
        ], null=True)

    priority = models.CharField(max_length = 150,blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'
    
    def __str__(self) -> str:
        return f"{self.contract_title} - {self.code}"
    
    