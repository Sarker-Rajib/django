from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact-us/', include('Contact_us.urls')),
    path('services/', include('Service.urls')),
    path('patient/', include('Patient.urls')),
    path('doctor/', include('Doctor.urls')),
    path('appoinment/', include('Appoinment.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)