from django.db import models
import uuid
from plugins.dropdown import *



class DrawingBank(models.Model):
    code  = models.CharField(max_length=200)
    title = models.CharField(max_length = 150)
    description = models.TextField()
    created = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Drawing Bank'
        verbose_name_plural = 'Drawing Bank'

    

    def action(self):
        modalname = self._meta.model.__name__
        action = [
                # {"name":'Profile', "href":f"employee-profile", "is_button":False, 
                # "query":{'id':self.id}},
                ]
                
        return singleDropdown(
            action=action,
            code=self.code, 
            modelname=modalname,
            report_template_name='tasks',
            is_report=False, 
            report_title='Employee',
            link='/admin/reports/get-report'
        )
    
    