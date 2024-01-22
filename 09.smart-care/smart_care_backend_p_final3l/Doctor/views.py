from rest_framework import viewsets
from .serializers import DesignationSerialysers, DoctorSerialysers, SpecializationSerialysers, AvailableTimeSerialysers, Doctor, Designation, AvailableTime, Specialization, Review, ReviewSerialysers
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

# Create your views here.
class DesignationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Designation.objects.all()
    serializer_class = DesignationSerialysers

class SpecificationViewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerialysers

class AvailableTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerialysers

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerialysers

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialysers