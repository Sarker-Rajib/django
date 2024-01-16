from rest_framework import viewsets
from .serializers import DesignationSerialysers, DoctorSerialysers, SpecializationSerialysers, AvailableTimeSerialysers, Doctor, Designation, AvailableTime, Specialization, Review, ReviewSerialysers

# Create your views here.
class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerialysers

class SpecificationViewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerialysers

class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerialysers

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerialysers

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialysers