from django.urls import path
from .views import add_post, EditPost, DeletePost, AddPostByClass, EditPostByClass, DeletePostByClass, DetailPostByClass

urlpatterns = [
    # path('add_post', add_post, name='add-post'),
    path('add_post', AddPostByClass.as_view(), name='add-post'),
    # path('edit-post/<int:id>', EditPost, name='edit-post'),
    path('edit-post/<int:id>/', EditPostByClass.as_view(), name='edit-post'),
    # path('delete-post/<int:id>', DeletePost, name='delete-post')
    path('delete-post/<int:id>/', DeletePostByClass.as_view(), name='delete-post'),
    path('details-post/<int:id>/', DetailPostByClass.as_view(), name='details-post')
]