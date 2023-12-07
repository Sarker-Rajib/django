from django import forms

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