from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
# Create your models here.


class Quotation(models.Model):
    code = models.CharField(max_length = 150, blank=True, null=True)
    name = models.CharField(max_length = 150, null=True)
    unit_price = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    qty  = models.IntegerField(verbose_name='Quantity', null=True)
    amount = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    created_at = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Quotation'
        verbose_name_plural = 'Quotations'
    
    def __str__(self) -> str:
        return f"{self.name} {self.unit_price} {self.qty} {self.amount}"




class LaborBillQuotation(models.Model):
    code = models.CharField(max_length = 150, null=True, blank=True)
    name = models.CharField(max_length = 150, null=True)
    activity = models.CharField(max_length = 150, verbose_name='Activity/Descriptions', null=True)
    unity_price = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    qty  = models.FloatField(verbose_name='Quantity', null=True)
    amount = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    date_time = models.CharField(max_length = 150, default='')
    created_at = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Labor Bill Quotation'
        verbose_name_plural = 'Labor Bill Quotation'
    
    def __str__(self) -> str:
        return f"{self.name} {self.unity_price} {self.qty} {self.amount}"