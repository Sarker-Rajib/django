from django.shortcuts import render, redirect
from .forms import Add_profile_form

# Create your views here.
def addProfile(request):
    if request.method == 'POST':
        addProfileForm = Add_profile_form(request.POST)
        if addProfileForm.is_valid():
            addProfileForm.save()
            return redirect('add-profile')
    else:
        addProfileForm = Add_profile_form()   
    return render(request, 'profile/add-profile.html', {'form': addProfileForm})