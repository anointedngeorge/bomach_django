from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
# Create your models here.


class Quotation(models.Model):
    name = models.CharField(max_length = 150)
    qty = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    unity_price = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    amount = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    created_at = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Quotation'
        verbose_name_plural = 'Quotations'
    
    def __str__(self) -> str:
        return self.name




class LaborBillQuotation(models.Model):
    name = models.CharField(max_length = 150)
    activity = models.CharField(max_length = 150)
    qty = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    unity_price = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    amount = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    created_at = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Labor Bill Quotation'
        verbose_name_plural = 'Labor Bill Quotation'
    
    def __str__(self) -> str:
        return self.name