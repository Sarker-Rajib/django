from django.shortcuts import render, redirect
# import forms
from django.contrib.auth.forms import AuthenticationForm
from .forms import User_Registration_form
# Import Validators / Authenticators
from django.contrib.auth import authenticate, login, logout
# import messages
from django.contrib import messages


# My views
def user_profile(request):
    return render(request, 'user/profile.html')

def user_register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            form = User_Registration_form(request.POST)
            print(form)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Created Successfully')
                return redirect('user_login')
            else:
                return redirect('register')
        else:    
            form = User_Registration_form()
            return render(request, 'user/register.html', {'form':form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data = request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                request_user = authenticate(username = user_name, password = user_pass)
                if request_user is not None:
                    login(request, request_user)
                    return redirect('home')
                else:
                    return redirect('login')
        else:
            form = AuthenticationForm()
            return render(request, 'user/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('user_login')