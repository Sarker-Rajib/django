from django.urls import path
from .views import AddPost

urlpatterns = [
    path('', AddPost, name='add-post')
]
