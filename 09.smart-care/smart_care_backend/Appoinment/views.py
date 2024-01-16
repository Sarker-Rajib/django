from rest_framework import viewsets
from .serializers import AppoinmentSerialysers, Appoinmentt

# Create your views here.
class AppoinmentViewset(viewsets.ModelViewSet):
    queryset = Appoinmentt.objects.all()
    serializer_class = AppoinmentSerialysers