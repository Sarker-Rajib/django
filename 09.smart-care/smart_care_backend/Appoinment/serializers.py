from rest_framework import serializers
from .models import Appoinmentt

class AppoinmentSerialysers(serializers.ModelSerializer):
    class Meta:
        model = Appoinmentt
        fields = '__all__'
