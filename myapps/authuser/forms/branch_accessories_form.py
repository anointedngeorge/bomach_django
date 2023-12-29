from django import forms
from django.db.models.query_utils import Q
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import MultipleChoiceField
from authuser.models.branch_model import (Branch, BranchAccessories)
from system_settings.models.model_types import Types

from authuser.fields import ListTextWidget

class BranchAccessoriesForm(forms.ModelForm):
  

    class Meta:
        model = BranchAccessories
        fields = ['branch','serial_number','name','assets_type','value_of_asset','status','description']
        widgets = {
            'assets_type':forms.Select(attrs={'class':'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(BranchAccessoriesForm, self).__init__(*args, **kwargs)
        # Types.objects.all()
        _datalist = kwargs.pop('data_list', None)
        # print(kwargs)
        self.fields['assets_type'].widget = ListTextWidget(data_list=_datalist, name='assets_type') 


