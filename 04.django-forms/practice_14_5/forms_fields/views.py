from django.shortcuts import render
from .forms import TestForm
# Create your views here.
def FormHome(request):
    M_form = TestForm()
    return render(request, 'form_plates/form-home.html', {'form': M_form})