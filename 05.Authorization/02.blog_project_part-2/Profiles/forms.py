from django import forms
from .models import Profile

class Add_profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        