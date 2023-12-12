from django.urls import path
from .views import add_task, taskMenu

urlpatterns = [
    path('', add_task, name='add-task'),
    path('tasks', taskMenu, name='taskmenu'),
]
