from django import forms
from .models import CustomJewelleryDesign

class CustomJewelleryDesignForm(forms.ModelForm):
    class Meta:
        model = CustomJewelleryDesign
        fields = '__all__'