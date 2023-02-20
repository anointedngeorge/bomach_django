from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.

from human_resource.models import *

class OperationProject(models.Model):
    name = models.CharField(max_length = 150, null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    
    class Meta:
    
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
    
    def __str__(self) -> str:
        return self.name
    
    