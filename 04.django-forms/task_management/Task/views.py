from django.shortcuts import render
from .forms import Task_Form

# Create your views here.
def add_task(request):
    return render(request, 'task/add-task.html', {'form': Task_Form})

def taskMenu(request):
    return render(request, 'task/task-menu.html')