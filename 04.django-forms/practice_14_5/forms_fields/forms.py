from django import forms
from django.forms.widgets import NumberInput
import datetime

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class TestForm(forms.Form):
    agree = forms.BooleanField()
    name = forms.CharField(max_length=35, label='Your name')
    comment = forms.CharField(widget=forms.Textarea)
    Opinion = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    email_address = forms.EmailField(required = False, label='Please enter your email address')
    first_name = forms.CharField(initial='Your name')
    agreeQ = forms.BooleanField(initial=True)
    TOday = forms.DateField(initial=datetime.date.today)
    favorite_color1 = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color2 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'd-inline'}), choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)

