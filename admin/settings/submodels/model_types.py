from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.

# from authuser.models import Branch



class Types(models.Model):
    CHOICE = [
        ('assets', 'Assets (Type)'),
    ]
    # branch = models.ForeignKey(Branch, on_delete=models.CASCADE, 
    # related_name='types_branch_rel')
    type =  models.CharField(max_length = 150, choices=CHOICE)
    name = models.CharField(max_length = 150)
    created = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
    
    def __str__(self) -> str:
        return self.name





