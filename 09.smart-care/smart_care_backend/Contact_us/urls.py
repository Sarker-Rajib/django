from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactUsViewset

router = DefaultRouter()
router.register('contact-us', ContactUsViewset)

urlpatterns = [
    path('', include(router.urls)),
]