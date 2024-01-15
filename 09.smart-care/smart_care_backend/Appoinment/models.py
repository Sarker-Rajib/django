from django.db import models
from django.contrib.auth.models import User
from Patient.models import Patient
from Doctor.models import Doctor, AvailableTime

# Create your models here.
APPOINMENT_STATUS = [
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Running','Running'),
]

APPOINMENT_TYPES = [
    ('Offline','Offline'),
    ('Online','Online'),
]

class Appoinmentt(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    appoinment_type = models.CharField(choices = APPOINMENT_TYPES, max_length = 20)
    appoinment_status = models.CharField(choices = APPOINMENT_STATUS, max_length = 20, default = 'Pending')
    symptom = models.TextField()
    time = models.OneToOneField(AvailableTime, on_delete = models.CASCADE)
    cancel = models.BooleanField(default = False)

    def __str__(self) -> str:
        return f'Patient : {self.patient.user.first_name}, Doctor : {self.doctor.user.first_name}'
