from django import forms
from .models import Festival, Artist

class FestivalForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = [
            'name', 
            'artists', 
            'website', 
            'date', 
            'time', 
            'latitude', 
            'longitude'
            ]
        
        
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
