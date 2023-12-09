from django.urls import path
from .views import AddPost, EditPost, DeletePost

urlpatterns = [
    path('', AddPost, name='add-post'),
    path('edit-post/<int:id>', EditPost, name='edit-post'),
    path('delete-post/<int:id>', DeletePost, name='delete-post')
]
