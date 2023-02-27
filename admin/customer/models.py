from django.db import models
import uuid
from authuser.models import User
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField


class Customer(models.Model):
    code = models.CharField(max_length = 150, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
     related_name="customer_relationship")
    country = CountryField(blank_label="(select country)", default='---',max_length=250)
    state = models.CharField(max_length=200, default='---')
    local_government = models.CharField(max_length=200, default='---')
    town = models.CharField(max_length=200, default='---')
    current_address = models.CharField(max_length=200, default='---')
    permanent_address = models.CharField(max_length=200, default='---')
    phone = models.CharField(max_length=200,  default='---')
    state = models.CharField(max_length=200, default='---')
    GENDER =[
        ('male','Male'),
        ('female','Female'),
        ('others','Others')
    ]
    gender =  models.CharField(max_length=250, choices=GENDER, default='---')
    notes = models.TextField(default='---')
    create_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Client"
        
    def __str__(self) -> str:
        return f"{self.user}"