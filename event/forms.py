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
            'longitude'
            ]
        
        
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.helper = FormHelper()
#             self.helper.form_method = 'post'
#             self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
#             self.helper.form_class = 'form-horizontal'  # Example: Add a form class

#             # Add CSS classes to specific fields (e.g., artists)
#             self.fields['artists'].widget.attrs['class'] = 'artist-checkboxes'

#             self.helper.layout = Layout(
#                 Div(
#                     Field('artists'), css_class="artist-checkboxes"
#                 ),
#                 Field('description'),

#             Field('artists', css_class="artist-checkboxes")
        
# )

        

    # def __init__(self, *args, **kwargs):
    #     super(FestivalForm, self).__init__(*args, **kwargs)
    #     self.fields['artists'].queryset = Artist.objects.all()
    #     self.fields['artists'].widget = forms.CheckboxSelectMultiple()

    def clean_website(self):
        website = self.cleaned_data.get('website')
        if website and not website.startswith(('http://', 'https://')):
            website = 'http://' + website
        return website