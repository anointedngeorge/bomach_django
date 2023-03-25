from django import forms
from django.db.models.query_utils import Q
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import MultipleChoiceField
from operations.models import *


class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ("__all__")
        widgets = {
            'email': forms.EmailInput(attrs={'onkeyup':'CheckClientAppointment(this.value)','class':'form-control'})
        }
        exclude = ('status','code')

    def __init__(self,*args,**kwargs):
         super(AppointmentForm,self).__init__(*args,**kwargs)
         self.fields['appointment_date'].error_messages = 'Appointment Date and Time already taken.'
        
    