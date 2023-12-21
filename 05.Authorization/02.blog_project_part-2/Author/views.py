from django.shortcuts import render, redirect
from .forms import AddAuthor

# Create your views here.
def viewAuthor(request):
    return render(request, 'authors/authors.html')

def addAuthor(request):
    if request.method == 'POST':
        author_form = AddAuthor(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add-author')

    else:
        author_form = AddAuthor
    
    return render(request, 'authors/add-author.html', {'form': author_form})