from django import forms
from . import models

class CarModelForm(forms.ModelForm):
    class Meta:
        model = models.CarModel
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.CommentModel
        fields = '__all__'