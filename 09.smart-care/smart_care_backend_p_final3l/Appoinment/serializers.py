from rest_framework import serializers
from .models import Appoinmentt

class AppoinmentSerialysers(serializers.ModelSerializer):
    time = serializers.StringRelatedField(many=False)
    patient = serializers.StringRelatedField(many=False)
    doctor = serializers.StringRelatedField(many=False)
    class Meta:
        model = Appoinmentt
        fields = '__all__'
