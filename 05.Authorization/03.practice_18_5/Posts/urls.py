from django.urls import path
from .views import add_post, EditPost, DeletePost

urlpatterns = [
    path('add_post', add_post, name='add-post'),
    path('edit-post/<int:id>', EditPost, name='edit-post'),
    path('delete-post/<int:id>', DeletePost, name='delete-post')
]
