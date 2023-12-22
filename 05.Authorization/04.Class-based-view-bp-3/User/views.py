from django.shortcuts import render, redirect
# import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from .forms import User_Registration_form, UpdateUserData
# Import Validators / Authenticators
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# import messages
from django.contrib import messages
# import required decorator
from django.contrib.auth.decorators import login_required
from Posts.models import Add_Post
from django.urls import reverse_lazy
# class based view import
from django.contrib.auth.views import LoginView, LogoutView


# My views
@login_required
def user_profile(request):
        if request.method == 'POST':
            form = UpdateUserData(request.POST, instance = request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Created Successfully')
                return redirect('profile')

        else:    
            form = UpdateUserData(instance = request.user)
        return render(request, 'user/profile.html', {'form':form})

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

# class based views
class UserLoginView(LoginView):
    template_name = 'user/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successful.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Logged-in Information Incorrect')
        return super().form_invalid(form)

class UserLogOutView(LogoutView):
    def get_success_url(self) -> str:
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Logged out successful.')


# -----------------------------
def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required
def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Updated Successfully')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, 'user/change-password.html', {'form': form})

@login_required
def update_password_eop(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)        
            return render(request, 'user/change-password.html', {'form': form})
    else:
        return redirect('login')

# Create your views here.
@login_required
def my_post(request):
    data = Add_Post.objects.filter(author = request.user)
    return render(request, 'user/my-post.html', {'data': data})





