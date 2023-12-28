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
    branch = models.ForeignKey(to='authuser.Branch', on_delete=models.CASCADE, 
    related_name='task_related_branch', null=True)
    user = models.ForeignKey(to='authuser.User', null=True, on_delete=models.CASCADE, 
    related_name="operation_rel")
    code = models.CharField(max_length = 150, null=True)
    task_category = models.ForeignKey(to='settings.Service',
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
    
    task_site  = models.ForeignKey(to='operations.OperationSite', on_delete=models.CASCADE, null=True, blank=True,
    related_name='task_site_rel')
    task_dependency  = models.ForeignKey(to="operations.OperationTask", on_delete=models.CASCADE, null=True, 
    blank=True, related_name='task_dependency_rel')

    start_date = models.DateField(auto_now=False, default='2023-05-01')
    end_date = models.DateField(auto_now=False, default='2023-05-01')
    assign_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='operations_task_employee')
    task_priority = models.CharField(max_length = 150, choices=[('high','High'),
    ('medium','Medium'), ('low','Low')])
    task_description = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    report_message = models.TextField(blank=True, null=True)
    
    STATUS = [
        ('pending','Pending'),
        ('todo','Todo'),
        ('doing','Doing'),
        ('completed','Completed'),
        ('redo','Redo'),
        ('suspended','Suspended')
    ]
    # todo: doing
    # doing: completed, redo
    # redo:suspended, completed, redo
    status = models.CharField(max_length = 150 , default='pending', choices=STATUS)
    created_at = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        permissions = (
            ("can_access_engineering_report", "Can Access Engineering Report"),
            ("can_access_survey_report", "Can Access Survey Report"),
            ("can_access_landing_report", "Can Access Landing Report"),

        )
    def __str__(self) -> str:
        return self.task_title

    def natural_key(self):
        return self.__str__()
    
    def get_profile(self):
        return f"{self.task_title}"
    
    def get_full_profile(self):
        return f"{self.task_title}"

    def action(self):
        try:
            modelname = self._meta.model.__name__
            action = {
                "pending": [
                    # {"name":f"{self.code}", "href":f"", "is_button":False, 
                    # "query":{'id':self.id}},
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
                is_report=False,
                link='/admin/reports/get-report',
            )
        except:
            pass
    