from django import forms
from .models import CustomJewelleryDesign


class CustomJewelleryDesignForm(forms.ModelForm):
    class Meta:
        model = CustomJewelleryDesign
        fields = '__all__'

    full_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    postcode = forms.CharField(max_length=20, required=False)
    town_or_city = forms.CharField(max_length=40, required=True)
    street_address1 = forms.CharField(max_length=80, required=True)
    street_address2 = forms.CharField(max_length=80, required=False)
    county = forms.CharField(max_length=80, required=False)    
