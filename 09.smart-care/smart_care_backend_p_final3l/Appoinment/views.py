from rest_framework import viewsets
from .serializers import AppoinmentSerialysers, Appoinmentt

# Create your views here.
class AppoinmentViewset(viewsets.ModelViewSet):
    queryset = Appoinmentt.objects.all()
    serializer_class = AppoinmentSerialysers

    # custom query
    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(queryset=queryset)
        return queryset