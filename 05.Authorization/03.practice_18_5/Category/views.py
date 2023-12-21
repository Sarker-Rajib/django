from django.shortcuts import render, redirect
from .forms import Add_Category_form
from .models import Add_Category
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


def DeleteC(request, id):
    selcted_post = Add_Category.objects.get(pk=id)
    selcted_post.delete()
    return redirect('add-category')