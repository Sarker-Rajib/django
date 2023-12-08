from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def model1(request):
    return render(request, 'model1.html')