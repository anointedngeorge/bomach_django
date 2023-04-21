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



Engineering_ADMIN_LIST = ['report_date','expenditure','expenditure2','report_site','status','action']

class EngineeringReport(ReportingSheet):
    # OperationSite,OperationProject
    code = models.CharField(max_length = 150, blank=True, null=True)
    report_date = models.DateField(auto_now=False, default=timezone.now, null=True)
    site_activities = RichTextField(null=True)
    report_site  = models.ForeignKey(on_delete=models.CASCADE, to="operations.OperationSite", related_name='eng_report', null=True)
    labor_and_bill = models.ManyToManyField(to='settings.LaborBillQuotation')
    expenditure = MoneyField(verbose_name="Expenditure Of Labor", 
    max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    material_received = models.ManyToManyField(to='operations.Stores', 
    verbose_name='material received and time')
    
    expenditure2 = MoneyField(verbose_name="Expenditure On Materials Received", 
    max_digits=10, decimal_places=2, null=True, default_currency='NGN')

    material_used = models.ManyToManyField(to='operations.StoreExpenditure')
    proposed_activity = RichTextField(null=True)
    materials_needed  = models.ManyToManyField(to='operations.stores', related_name='eng_material_rel')
    STATUS_CHOICE = [
        ('pending','Pending'),
        ('accepted','Accept'),
        ('rejected','Reject'),
    ]
    status = models.CharField(max_length = 150, choices=STATUS_CHOICE, default='pending')
    description = RichTextField(null=True, verbose_name='Comment')


    class Meta:
        verbose_name = 'Engineering Report'
        verbose_name_plural = 'Engineering Reports'
        permissions = (
            ("can_perform_extra_action", "Can perform extra action"),
        )

    def __str__(self) -> str:
        return f"{self.report_date}"

    def get_profile(self):
        return self.__str__()

    
    def get_full_profile(self):
        return f"{self.report_date}-({self.code})"

    def action(self):
        modelname = self._meta.model.__name__

        action = {
            'pending': [
                {"name":f"Accept", "href":f"", "is_button":False, 
                "query":{'id':self.id}},
                {"name":f"Reject", "href":f"", "is_button":False, 
                "query":{'id':self.id}},
            ],

            'accepted': [
                {"name":f"Print", "href":f"printout", "is_button":False, 
                "query":{'id':self.id}},
            ]


        }
        return dictDropdown(
            action=action, 
            status=self.status, 
            modelname=modelname, 
            code=self.code,
            show_media=True,
        )
    
    def _material_received(self):
        data = self.material_received.all()
        print(data)
        return 23
    
    
    
    
    
    
    

    
    




    
    