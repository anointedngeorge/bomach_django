from django.db import models
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin,
    BaseUserManager,
    UserManager
)
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField

GROUP_ROLES = [
    ('staff','Staff'),
    ('customer','Customer')
]

# Salutation - Mr, Mrs, Mr and Mrs, miss, Dr, Sir, Madam
SALUTATION = [
    ('---','Choose'),
    ('mr','Mr'),
    ('Mrs','Mrs'),
    ('miss','Miss'),
    ('dr','Dr'),
    ('sir','Sir'),
    ('madam','Madam')
]

import os
import sys
sys.path.append(os.path.abspath('../plugins'))

class CustomUserManager(UserManager):
    
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a vaild email address")

        email = self.normalize_email(email)
        user =  self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email, password, **extra_fields)


    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)
        

class User(AbstractBaseUser, PermissionsMixin):
    code = models.CharField(max_length=300, blank=True, null=True)
    email = models.EmailField(('email address'), unique=True, error_messages="Email Already Taken")
    username = models.CharField(max_length=300, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    roles = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, related_name='roles_rel')
    roles_name = models.CharField(max_length=300, blank=True, choices=GROUP_ROLES, null=True)
    picture_url = models.CharField(max_length=300, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=timezone.now())
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return f"{self.username}"

    def get_full_name(self):
        return f"{self.username}"
    
    def get_username(self):
        return f"{self.username}"
        # return self.email
    
    def get_short_name(self):
        return f"{self.username}" or self.email.split('@')[0]

    def natural_key(self):
        return f"{self.username}"

 


# distinguise
class Staff(User):
    salutation = models.CharField(max_length=300, choices=SALUTATION, default='---')
    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)
    surname = models.CharField(max_length=300, blank=True, null=True)
    
    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"
        
    def __str__(self) -> str:
        return f"{self.first_name}"

    def list_display(self):
        return ['pk']
    def list_display_links(self):
        return ['pk']
    def exclude(self):
        return []
    def has_action(self):
        return False
    def is_registered(self):
        return True
    
    def action(self):
        from plugins.dropdown import table_dropdown
        data = [
            {"name":"Sales", "url":f"property-sales-report/", "modal":True},
        ]
        return table_dropdown(title="Choose", content=data )




class Customer(User):
    salutation = models.CharField(max_length=300, choices=SALUTATION, default='---')
    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)
    surname = models.CharField(max_length=300, blank=True, null=True)
    
    class Meta:
        verbose_name = "Customers"
        verbose_name_plural = "Customers"

    def __str__(self) -> str:
        return f"{self.first_name}"
    
    def list_display(self):
        return ['pk']
    def list_display_links(self):
        return ['pk']
    def exclude(self):
        return []
    def has_action(self):
        return False
    def is_registered(self):
        return True
    
    def action(self):
        from plugins.dropdown import table_dropdown
        data = [
            {"name":"Sales", "url":f"property-sales-report/", "modal":True},
        ]
        return table_dropdown(title="Choose", content=data )
