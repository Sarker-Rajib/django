from django.urls import path
from .views import formOne

urlpatterns = [
    path('', formOne),
    path('form-1/', formOne, name='forms'),
]
