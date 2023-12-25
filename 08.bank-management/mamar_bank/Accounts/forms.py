from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .constants import gender_type, acc_type
from .models import UserAddress, UserBankAccount

class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    Acctp = forms.ChoiceField(choices=acc_type, label='Account Type')
    gender = forms.ChoiceField(choices=gender_type)
    street_address=forms.CharField(max_length=100)
    city=forms.CharField(max_length=100)
    country=forms.CharField(max_length=100)
    postal_code=forms.IntegerField()

    class Meta:
        model= User
        fields = ['username', 'first_name', 'last_name', 'email', 'birth_date', 'gender','Acctp', 'postal_code', 'country', 'city', 'street_address']
    
    def save(self, commit=True):
        new_user = super().save(commit=False)
        if commit == True:
            new_user.save()
            Acctp=self.cleaned_data['Acctp']
            birth_date=self.cleaned_data['birth_date']
            gender=self.cleaned_data['gender']
            postal_code=self.cleaned_data['postal_code']
            country=self.cleaned_data['country']
            city=self.cleaned_data['city']
            street_address=self.cleaned_data['street_address']
            
            UserAddress.objects.create(
                user = new_user,
                postal_code = postal_code,
                country = country,
                city = city,
                street_address = street_address
            )

            UserBankAccount.objects.create(
                user = new_user,
                Acctp = Acctp,
                gender = gender,
                birth_date = birth_date,
                account_no = 100000 + new_user.id
            )
        return new_user
    
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })

