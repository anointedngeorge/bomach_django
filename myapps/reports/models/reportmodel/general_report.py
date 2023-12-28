from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.

from human_resource.models import *
from customer.models import Customer
from system_settings.models.model_service import ServiceCategory
from operations.models.project_model import OperationProject
from operations.models.site_model import OperationSite
from django_countries.fields import CountryField
from plugins.dropdown import dictDropdown
from authuser.models.branch_model import Branch
from djmoney.models.fields import MoneyField
from plugins.dropdown import *
from reports.models.report_model import ReportingSheet
from datetime import datetime
from django.utils import timezone
from ckeditor.fields import RichTextField
from plugins.dropdown import *

LIST_GENERAL_REPORT = ['code','report_title','status','report_date','action']

class GeneralReport(ReportingSheet):
    ST2 = [
        ('pending', 'Pending'),
        ('incomplete', 'Incomplete'),
        ('to_do','To Do'),
        ('redo','Redo'),
        ('doing', 'Doing'),
        ('completed','Completed')
    ]
    # OperationSite,OperationProject
    code = models.CharField(max_length = 150,blank=True, null=True)
    user = models.ForeignKey(to="authuser.User", on_delete=models.CASCADE, blank=True, null=True)
    report_title = models.CharField(max_length = 150,blank=True, null=True)
    report_tasks = models.ManyToManyField(to="operations.OperationTask", related_name='general_report_rel')
    status = models.CharField(max_length = 150, choices=ST2, default='pending')
    report_date = models.DateField(auto_now=False, default=timezone.now)
    report_comment  = RichTextField()

    class Meta:
        verbose_name = 'General Report'
        verbose_name_plural = 'General Report'

    
    def __str__(self) -> str:
        return f"{self.report_title}- {self.report_date}"

    def get_full_profile(self):
        name =  f"{self.report_title} - {self.report_date}"
        return name
    
    def get_profile(self):
        name =  f"{self.report_title} - {self.report_date}"
        return name
    
    def action(self):
        modelname = self._meta.model.__name__
        action = {
            "pending": [
                # {"name":f"", "href":f"", "is_button":False, 
                # "query":{'id':self.id,'status':self.status,'title':self.name}},
            ],

        }
        return dictDropdown(action=action, show_media=True, status=self.status, modelname=modelname, code=self.code)

    
    

    
    




    
    