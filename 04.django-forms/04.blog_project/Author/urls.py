from django.urls import path
from .views import author

urlpatterns = [
    path('', author),
]
