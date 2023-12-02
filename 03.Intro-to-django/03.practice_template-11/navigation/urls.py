# from navigation

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.nav_home),
    path('about/<int:id>/', views.about, name='about'),
    path('contact/', views.contact),
]