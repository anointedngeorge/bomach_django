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

# name = models.CharField(max_length=50)
#     classes = models.ForeignKey(Classes, verbose_name=_("Class"), null=True, on_delete=models.CASCADE, related_name="section")
#     date = models.DateField(auto_now=True)



class RealEstate(models.Model):
    CHOICE = [
        ('soldout', 'Completedly Soldout'),
        ('avaliable', 'Can Still Sell Plots'),
    ]
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user_rel")
    branch = models.ForeignKey(Branch, verbose_name=("Choose Branch"), null=True, on_delete=models.CASCADE, related_name="branch_rel")

    # id=models.CharField(primary_key=True,default=uuid.uuid4, editable=False, max_length=36)
    name = models.CharField(max_length=500, null=True)
    total_amount = models.CharField(max_length=500, null=True)
    amount_deposited = models.CharField(max_length=500, null=True)
    unit_price = models.CharField(max_length=500, null=True)
    content = models.CharField(max_length=500, null=True)
    unique_code = models.CharField(max_length=500, null=True)
    is_blocked = models.BooleanField(default=False, null=True)
    is_featured = models.BooleanField(default=False, null=True)
    is_frontend = models.BooleanField(default=False, null=True)
    legal_fee = models.CharField(max_length=500, null=True)
    survey_plan = models.CharField(max_length=500, null=True)
    development_fee = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=500, null=True, choices=CHOICE, default='avaliable')
    created_at = models.DateField(auto_now=True)
    
    
    class Meta:
        verbose_name = "RealEstate"
        verbose_name_plural = "RealEstate"
        
    def __str__(self) -> str:
        return f"{self.name}"

    def action(self):
        action = {
            "soldout": [{"name":'sell', "href":'/', "is_button":False, "query":{'id':self.id}}, 
            {"name":'sell', "href":'/', "is_button":False, "query":{'id':self.id}},
            {"name":'sell', "href":'/', "is_button":False, "query":{'id':self.id}}
            ],
            "avaliable":    [{"name":'sell', "href":'', "is_button":False, "query":{'id':self.id}}],
        }
        return dictDropdown(action=action, status=self.status)


class RealEstatePlot(models.Model):
    CHOICE = [
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('reserved', 'Reserved'),
    ]
    # id=models.CharField(primary_key=True,default=uuid.uuid4, editable=False, max_length=36)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user_realestate_plot_rel")
    realestate = models.ForeignKey("Realestate", verbose_name=("Realestate"), null=True, on_delete=models.CASCADE, related_name="realestate_rel")
    
    name = models.CharField(max_length=500, null=True)
    price = models.CharField(max_length=500, null=True)
    size = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=500, null=True, 
    default='pending', choices=CHOICE)
    content = models.CharField(max_length=500, null=True)
    timer_date = models.DateField(auto_now=False, null=True)
    timer = models.TimeField(auto_now=False, null=True)
    transactional_code = models.CharField(max_length=500, null=True)
    purchase_code = models.CharField(max_length=500, null=True)
    unique_code = models.CharField(max_length=500, null=True)
    resell_code = models.CharField(max_length=500, null=True)
    payment_id = models.CharField(max_length=500, null=True)
    is_blocked = models.BooleanField(default=False, null=True)
    is_featured = models.BooleanField(default=False, null=True)
    is_frontend = models.BooleanField(default=False, null=True)
    is_sold = models.BooleanField(default=False, null=True)
    created_at = models.DateField(auto_now=True)

    
    # return format_html('<a href="{}" title="dowload_result" class="btn btn-sm btn-warning">Download Result</a>',
    #         reverse_lazy("admin:download-result-termly", 
    #             args=[])
    #     )
    def action(self):
        action = {
            "pending": [{"name":'sell plot', "href":'/', "is_button":False, "query":{'id':self.id, 'status':self.status}}, 
            {"name":'reserve', "href":'/', "is_button":False, "query":{'id':self.id}},
            ],
            "sold":    [{"name":'sell', "href":'', "is_button":False, "query":{'id':self.id}}],
            "reserved":[{"name":'reserved', "href":'', "is_button":False, "query":{'id':self.id}}],
        }
        return dictDropdown(action=action, status=self.status)