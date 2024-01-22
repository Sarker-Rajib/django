from django.contrib import admin
from .models import Appoinmentt
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Register your models here.
class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'doctor_name', 'appoinment_type', 'appoinment_status', 'symptom', 'time', 'cancel']
    def patient_name(self, obj):
        return obj.patient.user.first_name

    def doctor_name(self, obj):
        return obj.doctor.user.first_name
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appoinment_status == "Running" and obj.appoinment_type == 'online':
            # Email configuration
            email_subject = 'Your appoinment'
            email_body = render_to_string('appoinment-mail.html', {'User' : obj.patient.user, 'doctor' : obj.doctor})
            
            # Send email
            email = EmailMultiAlternatives(email_subject, '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()

admin.site.register(Appoinmentt, AppoinmentAdmin)