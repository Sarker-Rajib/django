from django.shortcuts import render
from rest_framework import viewsets
from . import serializers, models

# Create your views here.
class ContactUsViewset(viewsets.ModelViewSet):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializers