from django import forms
from .models import Musician, Album

class Artist_form(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'

class Album_form(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'rating' : forms.RadioSelect(),
            'ReleaseDate' : forms.DateInput(),
        }
