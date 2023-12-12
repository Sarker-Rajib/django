from django.urls import path
from .views import addMusician, add_album

urlpatterns = [
    path('add_artist', addMusician, name='add-artist'),
    path('add_album', add_album, name='add_album'),
]
