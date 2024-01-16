from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import DesignationViewset, SpecificationViewset, DoctorViewset, AvailableTimeViewset, ReviewViewset

router = DefaultRouter()

router.register('list', DoctorViewset)
router.register('designation', DesignationViewset)
router.register('specification', SpecificationViewset)
router.register('available-time', AvailableTimeViewset)
router.register('reviews', ReviewViewset)

urlpatterns = [
    path('', include(router.urls))
]