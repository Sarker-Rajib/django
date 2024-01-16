from rest_framework import viewsets
from . import serializer, models

# Create your views here.
class PatientViewset(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializer.PatientSerializers