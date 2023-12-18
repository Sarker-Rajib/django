from django.shortcuts import render, redirect
from .forms import RegisterFrom, UserDataChange
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'f_app/profile.html', {'user': request.user})
    else:
        return redirect('login')

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterFrom(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Created Successfully')
                return redirect('register')
        else:
            form = RegisterFrom()
        return render(request, 'f_app/register.html', {'form': form})
    else:
        return redirect('profile')
    
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username = name, password = password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')                    
        else:
            form = AuthenticationForm()
        return render(request, 'f_app/login.html', {'form':form})
    else:
        return redirect('profile')

def user_logout(request):
    logout(request)
    return redirect('login')

def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)        
        return render(request, 'f_app/change-pass.html', {'form':form})
    else:
        return redirect('login')

def change_pass2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)        
        return render(request, 'f_app/change-pass.html', {'form':form})
    else:
        return redirect('login')
    
def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserDataChange(request.POST, instance= request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Update Successfully')
                return redirect('profile')
        else:
            form = UserDataChange(instance= request.user)
        return render(request, 'f_app/register.html', {'form': form})
    else:
        return redirect('login')
  
