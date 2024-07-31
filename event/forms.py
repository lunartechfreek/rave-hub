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
            'location_name',
            'latitude', 
            'longitude',
            'featured_image'     
            ]

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'name': forms.TextInput(attrs={'autocomplete': 'on'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

    def clean_website(self):
        website = self.cleaned_data.get('website')        
        if website:
            if website.startswith('http://'):
                website = 'https://' + website[7:]
            elif not website.startswith('https://'):
                website = 'https://' + website
        return website