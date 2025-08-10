from .models import Location
from django import forms

class LocationForm(forms.ModelForm):

    address_1 = forms.CharField(required=True)
    zip_code = forms.CharField(required=True)

    class Meta:
        model = Location
        fields = {'address_1', 'address_2', 'city', 'state', 'zip_code'}