from django import forms
from .models import Festival, Artist

class FestivalForm(forms.ModelForm):
    artists = forms.ModelMultipleChoiceField(
        queryset = Artist.objects.order_by('name'),
        widget = forms.CheckboxSelectMultiple(attrs={"class": "artist-checkboxes"}),
        required = True,
        )

    class Meta:
        model = Festival
        fields = [
            'name', 
            'artists', 
            'website', 
            'date', 
            'time', 
            'latitude', 
            'longitude',
            'location_name'
            ]
        
        
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'name': forms.TextInput(attrs={'autocomplete': 'on'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

    def clean_website(self):
        website = self.cleaned_data.get('website')
        if website and not website.startswith(('http://', 'https://')):
            website = 'https://' + website
        return website