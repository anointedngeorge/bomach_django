from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.



class Service(models.Model):
    CHOICE =  [
        ('child', 'Child'),
        ('parent','Parent')
    ]
    status  = models.CharField(max_length = 150, null=True, blank=True, choices=CHOICE, default='parent')
    name = models.CharField(max_length = 150)
    parent_to  = models.ForeignKey(verbose_name='Parent', to='system_settings.Service', on_delete=models.CASCADE, 
    related_name='service_parent_rel', null=True, blank=True, default=None
    )
    is_child_to = models.ForeignKey(verbose_name='Child', to='system_settings.Service', on_delete=models.CASCADE, blank=True, null=True,
    related_name='child_service_model'
    )
    description  = models.TextField(blank=True)
    
    
    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Service'
    
    def __str__(self) -> str:
        return self.name

    def natural_key(self):
        return self.__str__()



class ServiceCalculator(models.Model):
    FUNCTIONS = [
        ('function1','Function1'),
        ('general_engine_calc','General Engine Calculator')
    ]
    name = models.CharField(max_length = 150, null=True, verbose_name='Title')
    service = models.ForeignKey(to="system_settings.Service", on_delete=models.CASCADE, null=True)
    up = models.IntegerField(default=0, verbose_name='unit price')
    ebb =  models.IntegerField(default=0, verbose_name='Extra bedroom unit Price')
    efb =  models.IntegerField(default=0, verbose_name='Extra floor bill')
    esrup =  models.IntegerField(default=0, verbose_name='Extra Sitting Room Unit Price')
    nb =  models.IntegerField(default=0, verbose_name='Number of bedroom')
    nf =  models.IntegerField(default=0, verbose_name='Number of floor')
    ns =  models.IntegerField(default=0, verbose_name='Number of sitting room')
    mncb =  models.IntegerField(default=0, verbose_name='Maximum number of category bedroom')
    mncf =  models.IntegerField(default=0, verbose_name='Maximum number of category floor')
    mncs =  models.IntegerField(default=0, verbose_name='Maximum number of category sitting room')
    total = models.IntegerField(default=0)
    
    function = models.CharField(max_length = 150,
    blank=True, null=True, 
    choices=FUNCTIONS, 
    help_text='Choose a function to calculate with!')
    
    
    class Meta:
        verbose_name = 'Services Calculator'
        verbose_name_plural = 'Service Calculator'
    
    def __str__(self) -> str:
        return f"{self.service}"
    
    def natural_key(self):
        return self.__str__()





class ServiceCategory(models.Model):
    name = models.CharField(max_length = 150)
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE,
     related_name="hr_service_relationship", null=True)
    # service = models.ManyToManyField(Service)

    name = models.CharField(max_length = 150)
    description  = models.TextField()
    
    class Meta:
        verbose_name = 'Services Category'
        verbose_name_plural = 'Service Category'
    
    def __str__(self) -> str:
        return self.name




