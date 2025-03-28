from django.db import models
import uuid
from django.core import serializers
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.
from plugins.dropdown import singleDropdown, dictDropdown
from authuser.models import Branch
# from phonenumber_field.modelfields import PhoneNumberField


class EmployeeType(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Employement Type'
        verbose_name_plural = 'Employment Type'

    def natural_key(self):
        return self.__str__()


class Designation(models.Model):
    roles  = models.ManyToManyField(to="human_resource.Jobs", blank=True)
    name = models.CharField(max_length = 150)
    description = models.TextField()

    class Meta:
        verbose_name = 'Designation'
        verbose_name_plural = 'Designation'
    
    def __str__(self) -> str:
        return self.name

    def natural_key(self):
        return self.__str__()


class Employee(models.Model):
    code = models.CharField(max_length = 150, null=True)
    special_roles  = models.ManyToManyField(to="human_resource.Jobs", blank=True)
    branch = models.ForeignKey(to='authuser.Branch',verbose_name='branch', on_delete=models.CASCADE, null=True, blank=True,
     related_name="hr_branch_employee_relationship")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='employee',  on_delete=models.CASCADE, null=True, blank=True,
     related_name="hr_employee_relationship")
    #  personal information
    address = models.CharField(max_length=500, null=True, default='---')
    phone_number = models.CharField(max_length=500, null=True, default='---')
    dob = models.DateField(auto_now=False, default='2023-04-01')

    designation =  models.ForeignKey(Designation, on_delete=models.CASCADE, null=True, blank=True,
     related_name="employee_designation_relationship", default=None)
    title =  models.ForeignKey("Jobs", on_delete=models.CASCADE, null=True, blank=True,
     related_name="employee_job_relationship")
    department =  models.ForeignKey("Department", on_delete=models.CASCADE, null=True, blank=True,
     related_name="employee_department_relationship")
    employment_type =  models.ForeignKey("EmployeeType", on_delete=models.CASCADE, null=True, blank=True,
     related_name="employee_department_type_relationship")
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
    state = models.CharField(max_length=50, null=True, default='---')
    local_government = models.CharField(max_length=250, default='---')
    town = models.CharField(max_length=250, null=True, default='---')
    salary = models.CharField(max_length=250, null=True, default='---')
    about = models.TextField(default='---')
    start_date = models.DateField(auto_now=True)
    probation_start_date  = models.DateField(auto_now=True)
    probation_end_date  = models.DateField(auto_now=True)
    JOBSTATUS =[
        ('proposed','Proposed'),
        ('retired','Retired'),
        ('probation','On Probation'),
    ]
    status =  models.CharField(max_length=250, choices=JOBSTATUS, default='proposed')
    skills = models.ManyToManyField('Skill', blank=True)
    
    create_at = models.DateField(auto_now=True)
    last_created = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employee"
        
    def __str__(self) -> str:
        return f"{self.user}"


    def natural_key(self):
        return self.__str__()

    def action(self):
        modalname = self._meta.model.__name__
        action = [
                # {"name":'Profile', "href":f"employee-profile", "is_button":False, 
                # "query":{'id':self.id}},
                ]
        
        return singleDropdown(
            action=action, 
            modelname=modalname,
            report_template_name='tasks',
            is_report=False, 
            report_title='Employee',
            link='/admin/reports/get-report'
        )


    def get_fullname(self):
        employee_name =  f"{self.user.first_name} {self.last_name}" if self.user.surname != None else f"{self.user.first_name} {self.user.last_name}"
        return employee_name

    
    def get_related_task(self):
        task = self.operations_task_employee.all()
        return task
    
    
    def get_related_projects(self):
        relatedNames =  self.project_members_rel.all()
        return relatedNames