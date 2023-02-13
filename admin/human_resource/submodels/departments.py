from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.

from human_resource.models import *

class Department(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField()
    
    
    