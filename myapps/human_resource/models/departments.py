from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.

from human_resource.models import *

class Department(models.Model):
    code = models.CharField(max_length = 150, null=True)
    name = models.CharField(max_length = 150)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.name

    def natural_key(self):
        return self.__str__()
    
    