from django.urls import path
from .views import FormHome
urlpatterns = [
    path('', FormHome, name='forms'),
]