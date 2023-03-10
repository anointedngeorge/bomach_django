from django.db import models

# Create your models here.
from operations.submodels.contract_model import *
from operations.submodels.project_model import *
from operations.submodels.site_model import *
from operations.submodels.task_model import *


# for reporting

from operations.submodels.reportmodel.general_report import *
from operations.submodels.reportmodel.engineering_site_report import *
from operations.submodels.reportmodel.land_survey import *
