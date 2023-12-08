from django.urls import path, include
from . import views

urlpatterns = [
    path('first-model', views.firstModel, name='first-model'),
    path('delete/<int:roll>', views.delete_student, name='delete_student'),
]