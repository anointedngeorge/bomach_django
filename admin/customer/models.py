from django.db import models
import uuid
from authuser.models import User
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField



CUSTOMER_ADMIN_LIST = ['code','fullName','country','phone','gender','projects','sites']


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
        return f"{self.user.first_name} {self.last_name}"



    def get_client_fullname(self):
        return self.__str__()

    def natural_keys(self):
        return self.__str__()

    def fullName(self):
        return f"{self.user}"
        

    def projects(self):
        pro = self.client_rel.all().count()
        return f"{pro}"
    
    def sites(self):
        site_count = self.site_client_rel.all().count()
        return f"{site_count}"


    def get_related_sites(self):
        sites = self.site_client_rel.all()
        return sites


    def get_related_projects(self, dt1=None):
        relatedNames =  self.client_rel.all()
        return relatedNames