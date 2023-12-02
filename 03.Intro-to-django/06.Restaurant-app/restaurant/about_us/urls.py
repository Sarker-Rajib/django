from django.contrib import admin
from django.urls import path
from . import views

# about us

urlpatterns = [
    path('', views.home, name='about-us'),
]