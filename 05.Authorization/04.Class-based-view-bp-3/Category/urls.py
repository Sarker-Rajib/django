from django.urls import path
from .views import add_category, DeleteC

urlpatterns = [
    path('add_category', add_category, name='add-category'),
    path('d/<int:id>', DeleteC),
]
