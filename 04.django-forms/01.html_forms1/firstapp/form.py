from typing import Any
from django import forms
from django.core import validators

# widgets == field to html input

class contactform(forms.Form):
    fname = forms.CharField(label='Username')
    comment = forms.CharField(label='Comment', widget=forms.Textarea(attrs={'id': 'comment', 'class': 'forms-man', 'placeholder': 'Your comment'}))
    # file = forms.ImageField(label='file')
    # email = forms.EmailField(label='User Email')
    age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appoinment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    # check = forms.BooleanField(label="Ensure You are agree")
    choises = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    order = forms.MultipleChoiceField(choices=choises, widget=forms.RadioSelect)
    Multiple = forms.ChoiceField(choices=choises, widget=forms.CheckboxSelectMultiple)
    name = forms.CharField(label='Last Name', initial='Sarker')
    check = forms.BooleanField(label="I am Agree", help_text='Please Check The checkbox', required=True)


# class studentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     # def clean_name(self):
#     #     valName = self.cleaned_data['name']
#     #     if len(valName) < 10:
#     #         raise forms.ValidationError('Enter a name with 10 char')
#     #     return valName

#     # def clean_email(self):
#     #     valEmail = self.cleaned_data['email']
#     #     if '.com' not in valEmail:
#     #         raise forms.ValidationError('must include .com')
#     #     return valEmail

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']

#         if len(valname) < 10:
#             raise forms.ValidationError('Enter a name with 10 char')
    
#         if '.com' not in valemail:
#             raise forms.ValidationError('must include .com')

class studentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='PLease enter min 10 char'), validators.MinLengthValidator(40, message='PLease enter max 40 char')])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid email')])

class PasswordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    checkPassword = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_pass_check = self.cleaned_data['checkPassword']
        if val_pass_check != val_pass:
            raise forms.ValidationError("Password Not matched")
