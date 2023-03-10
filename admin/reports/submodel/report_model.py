from django.db import models
from django.conf import settings





class ReportingSheet(models.Model):
    author  = models.CharField(max_length = 150, null=True)
    report_type  = models.CharField(max_length = 150, null=True)
    modelname  = models.CharField(max_length = 250, null=True)
    modelid  = models.IntegerField(default=1)
    created_at  = models.DateField(auto_now=True)
    
    
    class Meta:
        # abstract=True,
        verbose_name = 'All Reporting'
        verbose_name_plural = 'Reporting'
    