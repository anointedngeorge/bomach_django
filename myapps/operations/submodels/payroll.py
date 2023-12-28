from django.db import models
from django.utils import timezone

class PayRoll(models.Model):
    branch = models.ForeignKey(to='authuser.Branch', on_delete=models.CASCADE, 
    related_name='payroll_related')
    employee  = models.ForeignKey(to='human_resource.Employee', 
    on_delete=models.CASCADE, related_name='payroll_employee_rel')
    bonus  = models.IntegerField(null=True, blank=True)
    monthly_amount = models.IntegerField(null=True, blank=True)
    monthly_date = models.DateField(auto_now=False, default=timezone.now)
    created = models.DateField(auto_now=False, auto_now_add=False)
    
    
    
    
    
    
    