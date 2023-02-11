from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.

class Employee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
     related_name="employee_relationship")
    #  personal information
    address = models.CharField(max_length=500, null=True, default='---')
    phone_number = models.CharField(max_length=500, null=True, default='---')
    date_of_birth = models.DateField(auto_now=True)
    DESIGNATION = [
        ('trainee','Trainee'),
        ('senior','Senior'),
        ('junior','Junior'),
        ('teamlead','Team lead'),
        ('adhoc','Adhoc'),
    ]
    designation =  models.CharField(max_length=250, choices=DESIGNATION, default='---')
    TITLE = [
        ('civilengineer','Civil Engineer'),
        ('landsurveyor','Land Surveyor'),
        ('marketer','Marketer'),
        ('developer','Developer'),
        ('secretary','Secretary'),
        ('consultants','Consultants'),
        ('chiefsecurityofficer','Chief Security Officer'),
        ('securityofficer','Security Officer'),
        ('technician','Technician')
    ]
    title =  models.CharField(max_length=250, choices=TITLE, default='---')
    DEPARTMENT = [
        ('marketing','Marketing'),
        ('sales','Sales'),
        ('humanresources','Human Resources'),
        ('publicrelations','Public Relations'),
        ('research','Research'),
        ('financeandAccounts','finance and Accounts'),
        ('operations','Operations')
    ]
    department =  models.CharField(max_length=250, choices=DEPARTMENT, default='---')
    EMPLOYMENT_TYPE = [
        ('fulltime','Full Time'),
        ('parttime','Part Time'),
        ('oncontract','On Contract'),
        ('internship','Internship'),
        ('trainee','Trainee'),
    ]
    employment_type =  models.CharField(max_length=250, choices=DEPARTMENT, default='---')
    MARITAL_STATUS = [
        ('single','Single'),
        ('married','Married'),
        ('divorced','Divorced')
    ]
    marital_status =  models.CharField(max_length=250, choices=MARITAL_STATUS, default='---')
    GENDER =[
        ('male','Male'),
        ('female','Female'),
        ('others','Others')
    ]
    gender =  models.CharField(max_length=250, choices=GENDER, default='---')
    country = CountryField(blank_label="(select country)", default='---', max_length=200)
    local_government = models.CharField(max_length=250, default='---')
    town = models.CharField(max_length=250, null=True, default='---')
    about = models.TextField(default='---')
    skills = models.CharField(max_length=50, null=True, default='---')
    salary = models.CharField(max_length=50, null=True, default='---')
    start_date = models.DateField(auto_now=True)
    probation_start_date  = models.DateField(auto_now=True)
    probation_end_date  = models.DateField(auto_now=True)
    create_at = models.DateField(auto_now=True)
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employee"
        
    def __str__(self) -> str:
        return f"{self.user}"