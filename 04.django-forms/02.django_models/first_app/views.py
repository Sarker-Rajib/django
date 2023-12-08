from django.shortcuts import render, redirect
from . import models

# Create your views here.

def firstModel(request):
    student = models.Student.objects.all()
    print(student)
    return render(request, 'first_App/index.html', {'data':student})

def delete_student(request, roll):
    std = models.Student.objects.get(pk = roll).delete()
    return redirect('first-model')