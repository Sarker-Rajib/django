from django.shortcuts import render, redirect
from .forms import Add_Category_form
from django.contrib import messages

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        form = Add_Category_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Added Successfully')
            return redirect('add-category')
    else:
        form = Add_Category_form()
    return render(request, 'post/add-category.html', {'form': form})