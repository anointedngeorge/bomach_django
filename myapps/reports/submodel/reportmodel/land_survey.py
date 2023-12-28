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

LIST_LANDSURVERY_REPORT = ['repo']

class LandSurveyReport(ReportingSheet):
    # OperationSite,OperationProject
    report_sites = models.ManyToManyField(to="operations.OperationSite", related_name='engineering_sites_rel')
    client  = models.ForeignKey(to='customer.Customer', on_delete=models.CASCADE, blank=True, null=True)
    state_of_site = models.CharField(max_length = 150)
    site_activities = RichTextField(null=True)
    survey_equipment = RichTextField(null=True)
 
    labor_and_bill = models.ForeignKey(to='settings.LaborBillQuotation', related_name='land_bills_rel', on_delete=models.CASCADE, null=True)
    material_received = models.ForeignKey(verbose_name='material received and time', to='settings.Quotation', related_name='land_survey_rel', on_delete=models.CASCADE, null=True)
    proposed_activity = RichTextField(null=True)
    materials_needed = models.ForeignKey(to='settings.Quotation', related_name='land_material_need', on_delete=models.CASCADE, null=True)
    expenditure = MoneyField(verbose_name="Total Expenditure Of Labor", 
    max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    equipment = models.ForeignKey(to='settings.Quotation', 
    verbose_name='Surveying Expenditure on Labour', related_name='land_equipment_rel', on_delete=models.CASCADE, null=True)
    site_point_records = RichTextField(null=True)
    
    
    
    
    
    
    

    
    




    
    