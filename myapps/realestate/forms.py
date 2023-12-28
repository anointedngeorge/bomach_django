from django import forms
from django.db.models.query_utils import Q
from django.contrib.auth.forms import UserCreationForm
from authuser.models import User
from django.forms.fields import MultipleChoiceField
from .models import *


class realestateForm(UserCreationForm):

    """
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
    created_at = models.DateField(auto_now=True)
    """


    class Meta:
        model = RealEstate
        fields = ("name","total_amount","amount_deposited","unit_price")
        # exclude = ['password2']





