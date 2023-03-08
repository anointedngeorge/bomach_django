from django.db import models
import uuid
from authuser.models import (User, Branch)

from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# from ckeditor.fields import RichTextField
from django.utils.html import format_html
from django.urls import reverse_lazy
# Create your models here.
from plugins.dropdown import dictDropdown
from django.conf import settings
from customer.models import *
from plugins.url import (
    local_file_url_image,
    api_fetch_image
)
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from djmoney.models.fields import MoneyField

class RealEstate(models.Model):
    CHOICE = [
        ('soldout', 'Completedly Soldout'),
        ('avaliable', 'Can Still Sell Plots'),
    ]
    code = models.CharField(max_length = 150, null=True)
    
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user_rel")
    branch = models.ForeignKey(Branch, verbose_name=("Choose Branch"), null=True, on_delete=models.CASCADE, related_name="branch_rel")

    # id=models.CharField(primary_key=True,default=uuid.uuid4, editable=False, max_length=36)
    name = models.CharField(max_length=500, null=True)
    total_amount = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    amount_deposited = models.CharField(max_length=500, null=True)
    unit_price = models.CharField(max_length=500, default=0.01)
    content = models.CharField(max_length=500, null=True)
    unique_code = models.CharField(max_length=500, null=True)
    is_blocked = models.BooleanField(default=False, null=True)
    is_featured = models.BooleanField(default=False, null=True)
    is_frontend = models.BooleanField(default=False, null=True)
    legal_fee = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    survey_plan = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='NGN')
    development_fee = models.CharField(max_length=500, default=0.01)
    status = models.CharField(max_length=500, null=True, choices=CHOICE, default='avaliable')
    created_at = models.DateField(auto_now=True)
    
    
    class Meta:
        verbose_name = "RealEstate"
        verbose_name_plural = "RealEstate"
        
    def __str__(self) -> str:
        return f"{self.name}"


    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

    def action(self):
        modelname = self._meta.model.__name__
       
        action = {
            "soldout": [{"name":f"{self.code}", "href":f"", "is_button":False, 
                "query":{'id':self.id,'status':self.status,'title':self.name}},

            {"name":'sell', "href":f"", "is_button":False, 
                "query":{'id':self.id,'status':self.status,'title':self.name }},

            {"name":'sell', "href":f"", "is_button":False, 
                "query":{'id':self.id,'status':self.status,'title':self.name }}
            ],
            
            "avaliable": [],
        }
        return dictDropdown(action=action, status=self.status, modelname=modelname, code=self.code)



