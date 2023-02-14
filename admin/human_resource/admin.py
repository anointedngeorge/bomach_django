from django.contrib import admin
from human_resource.models import *
from django.urls import path
from django.http import HttpResponse
# Register your models here.
# from fpdf import FPDF
from human_resource.subadmins.admin_employee import *
from human_resource.subadmins.admin_advert import *
from human_resource.subadmins.admin_department import *
from human_resource.subadmins.admin_employee_type import *
from human_resource.subadmins.admin_designation import *
from human_resource.subadmins.admin_jobs import *
from human_resource.subadmins.admin_salary import *
from human_resource.subadmins.admin_skills import *



    