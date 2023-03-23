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
from ckeditor.fields import RichTextField
from django.utils import timezone



class EngineeringReport(ReportingSheet):
    # OperationSite,OperationProject
    report_date = models.DateField(auto_now=False, default=timezone.now, null=True)
    site_activities = RichTextField(null=True)
    report_sites = models.ManyToManyField(to="operations.OperationSite")
    labor_and_bill = models.ManyToManyField(to='settings.LaborBillQuotation')
    material_received = models.ManyToManyField(to='operations.Stores', verbose_name='material received and time')
    material_used = models.ManyToManyField(to='operations.StoreExpenditure')

    proposed_activity = RichTextField(null=True)
    materials_needed  = models.ManyToManyField(to='operations.stores', related_name='eng_material_rel')
    expenditure = MoneyField(verbose_name="Expenditure Of Labor", 
    max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    description = RichTextField(null=True)
    
   
    
    
    
    
    
    
    

    
    




    
    