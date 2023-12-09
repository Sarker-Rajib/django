from django.shortcuts import render
from .forms import AddAuthor

# Create your views here.
def viewAuthor(request):
    return render(request, 'authors/authors.html')

def addAuthor(request):
    author_form = AddAuthor()
    return render(request, 'authors/add-author.html', {'form': author_form})