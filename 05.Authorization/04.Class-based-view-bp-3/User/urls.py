from django.urls import path
from .views import user_profile, UserLogOutView ,user_login, user_register, user_logout, update_password, my_post, update_password_eop, UserLoginView

urlpatterns = [
    path('', user_profile, name='profile'),
    path('my-post', my_post, name='myPosts'),
    path('register', user_register, name='register'),
    # path('login', user_login, name='user_login'),
    path('login', UserLoginView.as_view(), name='user_login'),
    # path('logout', user_logout, name='user_logout'),
    path('logout', UserLogOutView.as_view(), name='user_logout'),
    path('change-password', update_password, name='update_password'),
    path('change-password2', update_password_eop, name='update_password2'),
]