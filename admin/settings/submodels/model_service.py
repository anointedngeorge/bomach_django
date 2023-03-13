from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.



class Service(models.Model):
    name = models.CharField(max_length = 150)
    description  = models.TextField()
    
    
    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Service'
    
    def __str__(self) -> str:
        return self.name



class ServiceCategory(models.Model):
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




