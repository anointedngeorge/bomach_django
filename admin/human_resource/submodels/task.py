from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.
from human_resource.models import *
from settings.models import *


class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
     related_name="hr_task_user_relationship")
    name = models.CharField(max_length = 150)
    # category = models.ForeignKey("ServiceCategory", on_delete=models.CASCADE,
    #  related_name="task_service_category_relationship")
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    is_done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Task'
    
    def __str__(self) -> str:
        return self.name