from django.urls import path
from f_app import views

urlpatterns = [
    path('', views.home),
]