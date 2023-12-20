from django.urls import path
from .views import user_profile, user_login, user_register, user_logout, update_password

urlpatterns = [
    path('', user_profile, name='profile'),
    path('register', user_register, name='register'),
    path('login', user_login, name='user_login'),
    path('logout', user_logout, name='user_logout'),
    path('change-password', update_password, name='update_password'),
]
