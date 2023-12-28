from django import forms
from django.db.models.query_utils import Q
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import MultipleChoiceField
from operations.models.project_model import OperationProject


class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = OperationProject
        fields = ("__all__")
    
        