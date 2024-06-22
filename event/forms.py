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

    def clean_website(self):
        website = self.cleaned_data.get('website')
        if website and not website.startswith(('http://', 'https://')):
            website = 'http://' + website
        return website