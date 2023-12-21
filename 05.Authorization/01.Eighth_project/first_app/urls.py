from django.urls import path
from .views import user_login, register, profile, user_logout, change_pass, change_pass2, change_user_data

urlpatterns = [
    path('', profile, name='profile'),
    path('register', register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout,name='logout'),
    path('changePass', change_pass,name='changePass'),
    path('changePass2', change_pass2,name='changePass2'),
    path('updateUser', change_user_data, name='updateUser'),
]