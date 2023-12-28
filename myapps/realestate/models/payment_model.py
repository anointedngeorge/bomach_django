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
from realestate.models.plot_model import RealEstatePlot
from reports.models.payment_model import ReportPayment



class RealEstatePayment(ReportPayment):
    
    # id=models.CharField(primary_key=True,default=uuid.uuid4, editable=False, max_length=36)
    # user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="realestate_payment")
    plot = models.ForeignKey(RealEstatePlot, null=True, on_delete=models.CASCADE, 
    related_name="realestate_payment_plot")
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
    # total_amount = models.CharField(max_length=200, null=True)
    proxy = models.CharField(max_length=250, null=True)
    third_party_name = models.CharField(max_length=250, null=True)
    third_party_phone = models.CharField(max_length=250, null=True)
    third_party_email = models.CharField(max_length=250, null=True)
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
    

