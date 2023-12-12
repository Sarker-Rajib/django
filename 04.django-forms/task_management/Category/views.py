from django.shortcuts import render, redirect
from .forms import Category_form

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        form = Category_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addcategory')
    else:
        form = Category_form()
    return render(request, 'category/add-cat.html', {'form': Category_form})