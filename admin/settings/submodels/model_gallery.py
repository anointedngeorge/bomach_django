from django.db import models


from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField


class Gallery(models.Model):
    name = models.CharField(max_length = 150)
    size = models.CharField(max_length = 150)
    url = models.CharField(max_length=250, null=True)
    data = models.TextField(default='')
    filename  = models.CharField(max_length = 150, default='')
    type  = models.CharField(max_length = 150, default='')
    created_at = models.DateField(auto_now=True)
    



    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'
    
    def __str__(self) -> str:
        return self.name