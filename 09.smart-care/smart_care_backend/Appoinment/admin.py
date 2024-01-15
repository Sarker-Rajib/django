from django.contrib import admin
from .models import Appoinmentt

# Register your models here.
class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'doctor_name', 'appoinment_type', 'appoinment_status', 'symptom', 'time', 'cancel']
    def patient_name(self, obj):
        return obj.patient.user.first_name

    def doctor_name(self, obj):
        return obj.doctor.user.first_name
    
admin.site.register(Appoinmentt, AppoinmentAdmin)