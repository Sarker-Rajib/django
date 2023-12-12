from django.shortcuts import render

def HomePage(request):
    return render(request, 'Homepage.html')