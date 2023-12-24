from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from . import forms, models
from Cars.models import Car


# Create your views here.
@login_required
def user_profile(request):
    # bought_cars = models.MyCars.objects.all()
    myCars = models.MyCars.objects.filter(owner=request.user)
    return render(request, 'Users/profile.html', {'myCars': myCars})

def user_register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            inputForm = forms.RegisterUserForm(request.POST)
            if inputForm.is_valid():
                inputForm.save()
                messages.success(request, 'Account Created Successfully')
                return redirect('register')
            else:
                return redirect('login')
            
        else:
            inputForm = forms.RegisterUserForm(request.POST)
            return render(request, 'Users/register.html', {'form': inputForm})
    else:
        return redirect('profile')

class UserLogin(LoginView):
    form_class = AuthenticationForm
    template_name = 'Users/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successful.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged-in Information Incorrect')
        return super().form_invalid(form)
    
class UserLogOUt(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Logged out Successful.')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Updated Successfully')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, 'Users/change-password.html', {'form': form})

def update_profile_data(request):
    if request.method == 'POST':
        updateForm = forms.UpdateUser(request.POST, instance = request.user)
        if updateForm.is_valid():
            updateForm.save()
            messages.success(request, 'User Created Successfully')
            return redirect('profile')
    else:
        updateForm = forms.UpdateUser(instance = request.user)
        return render(request, 'Users/update-data.html', {'form':updateForm})

def buy_car(request, id):
    b_car = Car.objects.get(pk=id)
    b_car.quantity -= 1
    b_car.save()
    models.MyCars.objects.create(car=b_car, owner=request.user)
    return redirect('profile')