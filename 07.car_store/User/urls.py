from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='profile'),
    path('register/', views.user_register, name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogOUt.as_view(), name='logout'),
    path('change-pass/', views.change_password, name='change_password'),
    path('update-data/', views.update_profile_data, name='update_profile'),
    path('buy-car/<int:id>/', views.buy_car, name='buy_car'),
]