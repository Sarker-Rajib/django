from django.shortcuts import render
from .forms import User_Registration_form

# Create your views here.
def user_profile(request):
    return render(request, 'user/profile.html')

def user_register(request):
    form = User_Registration_form()
    return render(request, 'user/register.html', {'form':form})

def user_login(request):
    return render(request, 'user/login.html')
