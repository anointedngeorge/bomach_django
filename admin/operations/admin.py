from django.contrib import admin

# Register your models here.
from operations.subadmins.contract_admin import *
from operations.subadmins.project_admin import *
from operations.subadmins.site_admin import *
from operations.subadmins.task_admin import *


# reporting
from operations.subadmins.reportadmin.general_report_admin import *
from operations.subadmins.reportadmin.engineeringreport import *
from operations.subadmins.reportadmin.landsurveyreport import *