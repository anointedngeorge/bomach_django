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
            "soldout": [{"name":'sell', "href":f"", "is_button":False, 
                "query":{'id':self.id,'status':self.status,'title':self.name}},

            {"name":'sell', "href":f"", "is_button":False, 
                "query":{'id':self.id,'status':self.status,'title':self.name }},

            {"name":'sell', "href":f"", "is_button":False, 
                "query":{'id':self.id,'status':self.status,'title':self.name }}
            ],
            
            "avaliable": [{"name":'sell', "href":'', "is_button":False, 
                "query":{'id':self.id,'status':self.status,'title':self.name }}],
        }
        return dictDropdown(action=action, status=self.status)


class RealEstatePlot(models.Model):
    CHOICE = [
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('reserved', 'Reserved'),
        ('available','Available')
    ]
    # id=models.CharField(primary_key=True,default=uuid.uuid4, editable=False, max_length=36)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user_realestate_plot_rel")
    realestate = models.ForeignKey("Realestate", verbose_name=("Realestate"), null=True, on_delete=models.CASCADE, related_name="realestate_rel")
    customer = models.ForeignKey(Customer, null=True, 
    on_delete=models.CASCADE, related_name="customer_realestate_plot_rel")

    name = models.CharField(max_length=500, null=True)
    price = models.CharField(max_length=500, null=True)
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
            action = {
                "available": [
                    {"name":'sell plot', "href":f"sell-plot", "is_button":False, 
                "query":{'id':self.id, 'status':self.status,'title':f"{self.name} {self.realestate}"}}, 
                ],

                "pending": [
                    {"name":'Confirm Payment', "href":f"/admin/realestate/realestateplot/confirm-payment", "is_button":False, 
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
            return dictDropdown(action=action, status=self.status)
        except:
            pass

    def __str__(self) -> str:
        return self.name



class RealEstatePayment(models.Model):
    CHOICE = [
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('reserve', 'Reserved'),
    ]
    # id=models.CharField(primary_key=True,default=uuid.uuid4, editable=False, max_length=36)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="realestate_payment")
    plot = models.ForeignKey(RealEstatePlot, null=True, on_delete=models.CASCADE, related_name="realestate_payment_plot")
    status = models.CharField(max_length=500, null=True, default='pending', choices=CHOICE)
    activation_code = models.CharField(max_length=500, null=True)
    customer_email = models.CharField(max_length=500, null=True)
    purchase_code = models.CharField(max_length=500, null=True)
    customer = models.CharField(max_length=500, null=True)
    customer_phone = models.CharField(max_length=500, null=True)
    initial_amount = models.CharField(max_length=500, null=True)
    is_blocked = models.BooleanField(default=False, null=True)
    is_payment_activated = models.BooleanField(default=False, null=True)
    is_new_customer = models.BooleanField(default=False, null=True)
    is_confirmed = models.BooleanField(default=False, null=True)
    limited_date = models.CharField(max_length=200, null=True)
    total_amount = models.CharField(max_length=200, null=True)
    proxy = models.CharField(max_length=250, null=True)
    third_party_name = models.CharField(max_length=250, null=True)
    third_party_phone = models.CharField(max_length=250, null=True)
    third_party_email = models.CharField(max_length=250, null=True)
    created_at = models.DateField(auto_now=True)
    wait_confirmation = models.BooleanField(default=False, null=True)
    
    class Meta:
        verbose_name_plural = 'Payment'

    def __str__(self) -> str:
        return f"{self.customer} - {self.customer_email}"



class PaymentConfirmationRequest(models.Model):
    payment = models.ForeignKey(RealEstatePayment, null=True, 
    on_delete=models.CASCADE, related_name="realestate_payment_confirmation")
    user = models.ForeignKey(User, null=True, 
    on_delete=models.CASCADE, related_name="user_confirmation_payment")
    activation_code = models.CharField(max_length=500, null=True)
    activation_link = models.CharField(max_length=500, null=True)
    activation_link_code = models.CharField(max_length=500, null=True)
    is_payment_activated = models.BooleanField(default=False, null=True)
    created_at = models.DateField(auto_now=True)
    last_modified = models.DateField(auto_now=True)

    class Meta:
        managed = True
        verbose_name = 'Payment Request'
        verbose_name_plural = 'Payment Request'

    def __str__(self):
        return self.activation_code
    

