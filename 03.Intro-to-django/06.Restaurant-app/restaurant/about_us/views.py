from django.shortcuts import render

# Create your views here / about us.

def home(request):
    return render(request, 'about-us/index.html')