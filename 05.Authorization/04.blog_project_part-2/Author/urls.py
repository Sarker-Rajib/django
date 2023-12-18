from django.urls import path
from .views import viewAuthor, addAuthor

urlpatterns = [
    path('', viewAuthor, name='authors'),
    path('add', addAuthor, name='add-author')
]
