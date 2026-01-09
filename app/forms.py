from django import forms
from .models import AppVariaty

class AppVariatyForm(forms.Form):
    app_variety_name = forms.ModelChoiceField(queryset=AppVariaty.objects.all(), label='Select App Variety')
    
    
    
    