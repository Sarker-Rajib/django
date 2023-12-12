from django.urls import path
from .views import add_task, taskMenu, edit_task, delete_task

urlpatterns = [
    path('', add_task, name='add-task'),
    path('tasks', taskMenu, name='taskmenu'),
    path('edit/<int:id>', edit_task, name='edit-task'),
    path('delete/<int:id>', delete_task, name='delete-task'),
]
