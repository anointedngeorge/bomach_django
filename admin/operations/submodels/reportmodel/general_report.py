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
from plugins.dropdown import dictDropdown
from authuser.submodels.branch_model import Branch
from djmoney.models.fields import MoneyField
from plugins.dropdown import *
from reports.submodel.report_model import ReportingSheet
from datetime import datetime
from django.utils import timezone


class GeneralReport(ReportingSheet):
    # OperationSite,OperationProject
    task_title = models.CharField(max_length = 150, null=True)
    status = models.CharField(max_length = 150, choices=[
        ('incomplete', 'Incomplete'),
        ('to_do','To Do'),
        ('redo','Redo'),
        ('done', 'Done'),
        ('completed','Completed')
    ], null=True, blank=True)
    due_date = models.DateField(auto_now=False, default=timezone.now)
    task_start_date = models.DateField(auto_now=False, default=timezone.now)
    comment  = models.TextField()
    
    
    

    
    




    
    