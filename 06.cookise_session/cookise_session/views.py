from django.shortcuts import render

def home(request):
    response = render(request, 'index.html')
    response.set_cookie('name', 'hello')
    return response