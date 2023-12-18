from django.shortcuts import render , redirect
from .forms import Add_Category

# Create your views here.
def AddCategory(request):
    if request.method == 'POST':
        addProfileForm = Add_Category(request.POST)
        if addProfileForm.is_valid():
            addProfileForm.save()
            return redirect('add-category')
    else:
        addProfileForm = Add_Category()   
    return render(request, 'category/add-category.html', {'form': addProfileForm})