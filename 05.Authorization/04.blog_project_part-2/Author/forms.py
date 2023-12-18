from django import forms
from .models import Author
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AddAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        exclude = []