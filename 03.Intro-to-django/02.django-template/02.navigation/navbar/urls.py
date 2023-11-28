from django.contrib import admin
from django.urls import path, include
from . import views


# navbar app folder
urlpatterns = [
    path('about/', views.about),
    path('contact/', views.contact),
]