from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.

from human_resource.models import *
from settings.models import ServiceCategory
from customer.models import Customer
from django_countries.fields import CountryField
from operations.submodels.project_model import OperationProject
from plugins.dropdown import dictDropdown




class OperationSite(models.Model):
    site_code = models.CharField(max_length = 150, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, 
    related_name="operation_site_rel")
    code = models.CharField(max_length = 150, null=True)
    site_name = models.CharField(max_length = 150, null=True, blank=True)
    date_creation = models.DateField(auto_now=False, default='2023-03-02')
    service_category = models.ForeignKey(to="settings.Service", on_delete=models.CASCADE, null=True)
    site_client = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, related_name='site_client_rel')
    site_country = CountryField(blank_label="(select country)", default='---',max_length=250)
    site_lga = models.CharField(max_length=200, null=True, verbose_name='Site Local Government')
    site_state = models.CharField(max_length=200, null=True)
    site_map_location = models.TextField(null=True)
    scope_of_work = models.CharField(max_length = 150, null=True)
    stores = models.ManyToManyField(to='operations.Stores', related_name='site_store_rel', blank=True, null=True)
    project = models.ForeignKey(OperationProject, on_delete=models.CASCADE, 
    related_name='project_site_related', null=True)

    status = models.CharField(max_length = 150, choices=[
        ('completed','Completed'),
        ('rejected','Rejected'),
        ('pending','Pending')
        ], null=True)
    
    created_at = models.DateField(auto_now=True)
    
    
    class Meta:
    
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'
    
    def __str__(self) -> str:
        return f"{self.site_name}"

    def natural_key(self):
        return self.__str__()
    
    def action(self):
        modelname = self._meta.model.__name__

        action = {
            "pending": [{"name":f"{self.code}", "href":f"", "is_button":False, 
                "query":{'id':self.id}},
            ],
            "avaliable": [],
        }
        return dictDropdown(
            action=action, 
            status=self.status, 
            modelname=modelname, 
            code=self.code,
            report_template_name='site',
            report_title='Site Report',
            is_report=True,
            link='/admin/reports/get-report',
        )
    
    
    