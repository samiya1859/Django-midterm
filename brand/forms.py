from django import forms
from .models import BrandModel

class BrandModelForm(forms.ModelForm):
    class Meta:
        model = BrandModel
        fields = '__all__'