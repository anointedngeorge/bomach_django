from django import forms
from django.db.models.query_utils import Q
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import MultipleChoiceField
from operations.models import *


class EngineeringReportForm(forms.ModelForm):
    
    class Meta:
        model = EngineeringReport
        fields = ("__all__")
    
        