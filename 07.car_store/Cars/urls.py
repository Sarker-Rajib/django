from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.add_car, name='add-car'),
    path('car-details/<int:id>', views.CarDetails.as_view(), name='car_details'),
]