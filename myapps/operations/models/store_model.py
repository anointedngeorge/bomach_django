from django.db import models
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
from django.utils import timezone

STORE_ADMIN_LIST = ['name','activity','unit_price','qty','amount','site_code','is_site_taken','date_time']

class Stores(models.Model):
    site_code = models.CharField(max_length = 150, blank=True, null=True)
    is_site_taken = models.BooleanField(default=False, blank=True, null=True, verbose_name='Item In Use')
    code = models.CharField(max_length = 150, blank=True, null=True)
    # site = models.ForeignKey(to='operations.operationsite', on_delete=models.CASCADE, 
    # related_name='store_site', null=True)
    name = models.CharField(max_length = 150, null=True)
    activity = models.CharField(max_length = 150, verbose_name='Activity/Descriptions', null=True)
    unit_price = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    qty  = models.IntegerField(verbose_name='Quantity', null=True)
    amount = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    date_time  = models.CharField(max_length = 150, default='')
    created_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
    
    def __str__(self) -> str:
        return f"{self.name} has ${self.qty} at {self.amount}."


    

class StoreExpenditure(models.Model):
    store = models.ForeignKey(to='operations.Stores', on_delete=models.CASCADE, 
    related_name='Store_expenditure_site', null=True)
    # unity_price = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    qty  = models.IntegerField(verbose_name='Quantity', null=True)
    amount = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    created_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Store Expenditure'
        verbose_name_plural = 'Store Expenditures'
    
    def __str__(self) -> str:
        return f"{self.store} has ${self.qty} at {self.amount}."
    
    
    def natural_key(self):
        return self.__str__()
    
    