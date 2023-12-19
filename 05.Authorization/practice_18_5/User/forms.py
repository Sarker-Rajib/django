from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class User_Registration_form(UserCreationForm):
    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name']
        # fields= '__all__'
        