from rest_framework import serializers
from .models import Doctor, Specialization , Designation, AvailableTime, Review

class DoctorSerialysers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)
    designation = serializers.StringRelatedField(many = True)
    # designation = serializers.HyperlinkedRelatedField(many = True, view_name='designation', read_only=True)
    specialization = serializers.StringRelatedField(many = True)
    available_time = serializers.StringRelatedField(many = True)

    class Meta:
        model = Doctor
        fields = '__all__'

class SpecializationSerialysers(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class DesignationSerialysers(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class AvailableTimeSerialysers(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = '__all__'

class ReviewSerialysers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'