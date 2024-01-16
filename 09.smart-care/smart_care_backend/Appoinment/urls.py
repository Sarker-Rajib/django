from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AppoinmentViewset

router = DefaultRouter()

router.register('list', AppoinmentViewset)

urlpatterns = [
    path('', include(router.urls))
]