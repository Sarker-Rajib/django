from django.contrib import admin
from django.urls import path, include
from .views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('category/', include('Category.urls')),
    path('task/', include('Task.urls')),
    path('admin/', admin.site.urls),
]
