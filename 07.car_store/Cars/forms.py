from django import forms
from . import models

class AddCar(forms.ModelForm):
    class Meta:
        model = models.Car
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta: 
        model = models.Comment
        fields = ['name', 'body']
        widgets= {
          'body': forms.Textarea(attrs={'rows': 4})
        }