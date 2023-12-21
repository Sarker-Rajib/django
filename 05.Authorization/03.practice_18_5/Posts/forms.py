from django import forms
from .models import Add_Post

class Create_Post(forms.ModelForm):
    class Meta: 
        model = Add_Post
        exclude = ['author']