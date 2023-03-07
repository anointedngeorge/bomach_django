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
from djmoney.models.fields import MoneyField

class RealEstatePlot(models.Model):
    CHOICE = [
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('reserved', 'Reserved'),
        ('available','Available')
    ]
    code = models.CharField(max_length = 150, null=True)
    
    # id=models.CharField(primary_key=True,default=uuid.uuid4, editable=False, max_length=36)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user_realestate_plot_rel")
    realestate = models.ForeignKey("Realestate", verbose_name=("Realestate"), null=True, on_delete=models.CASCADE, related_name="realestate_rel")
    customer = models.ForeignKey(Customer, null=True, 
    on_delete=models.CASCADE, related_name="customer_realestate_plot_rel")

    name = models.CharField(max_length=500, null=True)
    price = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency=None)
    size = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=500, null=True, 
    default='available', choices=CHOICE)
    content = models.CharField(max_length=500, null=True)
    timer_date = models.DateField(auto_now=False, null=True)
    timer = models.TimeField(auto_now=False, null=True)
    transactional_code = models.CharField(max_length=500, null=True)
    purchase_code = models.CharField(max_length=500, null=True)
    unique_code = models.CharField(max_length=500, null=True)
    resell_code = models.CharField(max_length=500, null=True)
    payment_id = models.ForeignKey("RealEstatePayment", null=True, on_delete=models.CASCADE, related_name="realestate_payment_id_plot")
    is_blocked = models.BooleanField(default=False, null=True)
    is_featured = models.BooleanField(default=False, null=True)
    is_frontend = models.BooleanField(default=False, null=True)
    is_sold = models.BooleanField(default=False, null=True)
    has_ownership_changed = models.BooleanField(default=False, null=True)
    created_at = models.DateField(auto_now=True)

    
    # return format_html('<a href="{}" title="dowload_result" class="btn btn-sm btn-warning">Download Result</a>',
    #         reverse_lazy("admin:download-result-termly", 
    #             args=[])
    #     )
    def action(self):
        try:
            modelname = self._meta.model.__name__
            action = {
                "available": [
                    {"name":'sell plot', "href":f"sell-plot", "is_button":False, 
                "query":{'id':self.id, 'status':self.status,'title':f"{self.name} {self.realestate}"}}, 
                
                {"name":f"Upload Files", "href":f"{local_file_url_image(self.code)}", "is_button":False, 
                "query":{'id':self.id, 'model':modelname}}
                ],

                "pending": [
                    {"name":'Confirm Payment', "href":f"confirm-payment", "is_button":False, 
                    "query":{'id':self.id, 'status':self.status,'title':f"{self.name} {self.realestate}"}}, 

                    {"name":'Invoice', "href":f"invoice/{self.id}/", "is_button":False, 
                    "query":{'id':self.id, 'status':self.status,'title':f"{self.name} {self.realestate}"}},
                ],

                "sold": [{"name":'Receipt', "href":f"", "is_button":False, 
                "query":{'id':self.id,'status':self.status,'title':f"{self.name} {self.realestate}" } },
                {"name":'Change Ownership', "href":f"change-plot-ownership", "is_button":False, 
                "query":{'id':self.id,'status':self.status,'title':f"{self.name} {self.realestate}" } }
                ],

                "reserved":[{"name":'reserved', "href":f"", "is_button":False, 
                "query":{'id':self.id,'status':self.status,'title':f"{self.name} {self.realestate}" } }],
            }
            return dictDropdown(action=action, status=self.status, modelname=modelname, code=self.code)
        except:
            pass

    def __str__(self) -> str:
        return self.name


