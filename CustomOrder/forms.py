from django import forms
from .models import CustomJewelleryDesign

class CustomJewelleryDesignForm(forms.ModelForm):
    class Meta:
        model = CustomJewelleryDesign
        fields = ['design_name', 'jewellery_type', 'metal_type', 'stone_type', 'description', 'design_image']
