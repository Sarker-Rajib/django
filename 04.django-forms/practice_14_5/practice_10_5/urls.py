from django.contrib import admin
from django.urls import path, include
from .views import HomePage
urlpatterns = [
    path('', HomePage, name='home'),
    path('admin/', admin.site.urls),
    path('forms/', include('forms_fields.urls')),
]
