from django.shortcuts import render
from Musicians_directory.models import Musician

def home(request):
    data = Musician.objects.all()
    return render(request, 'Homepage.html', {'data': data})