from django.shortcuts import render, HttpResponse

# Create your views here.
def post(request):
    return HttpResponse('hello')