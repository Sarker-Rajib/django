from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='form-home'),
    path('about/', views.about, name='about'),
    path('djangoform/', views.djangoform, name='django-form'),
    path('valid-form/', views.studentForm, name='valid-form'),
    path('password-match/', views.passwordmatch, name='password-match'),
]