from django import forms
from .models import Add_Post, Comment

class Create_Post(forms.ModelForm):
    class Meta: 
        model = Add_Post
        exclude = ['author']
        widgets = {
            'category': forms.CheckboxSelectMultiple
        }

class Create_Comment(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body']