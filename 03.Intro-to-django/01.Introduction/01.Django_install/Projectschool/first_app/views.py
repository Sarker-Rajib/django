from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse("This is course page")

def fisrt_app(request):
    return HttpResponse("This is fp page")