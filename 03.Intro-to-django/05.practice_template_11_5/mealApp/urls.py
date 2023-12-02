from django.urls import path
from . import views

urlpatterns = [
    path('', views.indx, name='meal-home'),
    path('menu/', views.menu, name='meals'),
]