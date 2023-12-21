from django import forms
from .models import Add_Category

class Add_Category_form(forms.ModelForm):
    class Meta:
        model = Add_Category
        fields = '__all__'