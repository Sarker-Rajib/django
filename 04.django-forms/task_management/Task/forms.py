from django import forms
from .models import TaskModel

class Task_Form(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'