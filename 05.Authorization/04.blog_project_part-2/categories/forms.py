from django import forms
from .models import Category

class Add_Category(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'