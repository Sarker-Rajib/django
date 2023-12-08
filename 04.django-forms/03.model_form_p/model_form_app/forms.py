from django import forms
from .models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'roll': 'Student Roll',
            'name': 'Student name',
            'father_name': 'Fathers name'
        }
        widgets = {
            'roll': forms.PasswordInput()
        }
        help_texts = {
            'name': 'Write your full name'
        }

