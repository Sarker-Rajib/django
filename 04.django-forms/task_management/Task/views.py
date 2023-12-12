from django.shortcuts import render, redirect
from .forms import Task_Form
from .models import TaskModel

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = Task_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taskmenu')
    else:
        form = Task_Form()
    
    return render(request, 'task/add-task.html', {'form': Task_Form})

def taskMenu(request):
    data = TaskModel.objects.all()
    return render(request, 'task/task-menu.html', {'data': data})


def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    if request.method == 'POST':
        form = Task_Form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('taskmenu')
    else:
        form = Task_Form(instance=task)
    
    return render(request, 'task/edit-task.html', {'form': form})

def delete_task(request, id):
    print(request)
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('taskmenu')