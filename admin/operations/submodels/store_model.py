from django.db import models
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField




class Stores(models.Model):
    site = models.ForeignKey(to='operations.operationsite', on_delete=models.CASCADE, 
    related_name='store_site', null=True)
    name = models.CharField(max_length = 150, null=True)
    activity = models.CharField(max_length = 150, verbose_name='Activity/Descriptions', null=True)
    unit_price = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    qty  = models.IntegerField(verbose_name='Quantity', null=True)
    amount = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
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
    
    
    