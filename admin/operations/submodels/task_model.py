from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.

from human_resource.models import Employee
from operations.submodels.project_model import OperationProject
from settings.models import ServiceCategory
from operations.submodels.site_model import OperationSite
from plugins.dropdown import (dictDropdown, singleDropdown)


class OperationTask(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, 
    related_name="operation_rel")
    code = models.CharField(max_length = 150, null=True)
    task_category = models.ForeignKey(ServiceCategory,
    null=True,
    on_delete=models.CASCADE, 
    related_name='operations_task_service_category')
    task_title = models.CharField(max_length = 150)
    task_project = models.ForeignKey(OperationProject,
    default='---',
    on_delete=models.CASCADE,
    blank=True, null=True,
    related_name='operations_task_project')
    task_time = models.TimeField(auto_now=False, default='00:00:00')
    
    task_site  = models.ForeignKey(OperationSite, on_delete=models.CASCADE, null=True, blank=True,
    related_name='task_site_rel')
    task_dependency  = models.ForeignKey("OperationTask", on_delete=models.CASCADE, null=True, 
    blank=True, related_name='task_dependency_rel')

    start_date = models.DateField(auto_now=False, default='2023-05-01')
    end_date = models.DateField(auto_now=False, default='2023-05-01')
    assign_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='operations_task_employee')
    task_priority = models.CharField(max_length = 150, choices=[('high','High'),
    ('medium','Medium'), ('low','Low')])
    task_description = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)
    
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
    
    def __str__(self) -> str:
        return self.task_title
    

    def action(self):
        try:
            modelname = self._meta.model.__name__
            action = {
                "pending": [{"name":f"{self.code}", "href":f"", "is_button":False, 
                    "query":{'id':self.id}},
                ],
                "avaliable": [],
            }
            return dictDropdown(
                action=action, 
                status=self.status, 
                modelname=modelname, 
                code=self.code,
                report_template_name='tasks',
                report_title='Task Report',
                is_report=True,
                link='/admin/reports/get-report',
            )
        except:
            pass
    