from django.urls import path
from .views import AddCategory

urlpatterns = [
    path('', AddCategory, name='add-category'),
]