from django.urls import path
from .views import addProfile

urlpatterns = [
    path('', addProfile, name='add-profile'),
]
