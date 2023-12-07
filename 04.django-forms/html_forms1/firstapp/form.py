from django import forms

class contactform(forms.Form):
    name = forms.CharField(label='Username')
    email = forms.EmailField(label='User Email')
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    file = forms.ImageField()
    date = forms.DateField()
    appoinment = forms.DateTimeField()
    check = forms.BooleanField(label="Ensure You are agree")
    choises = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=choises)
    order = forms.MultipleChoiceField(choices=choises)
