from django.shortcuts import render, redirect
from .forms import Create_Post
from .models import Add_Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':
        form = Create_Post(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Post Added Successfully')
            return redirect('add-post')

    else:
        form = Create_Post()
    return render(request, 'post/add-post.html', {'form': form})

@login_required
def EditPost(request, id):
    selcted_post = Add_Post.objects.get(pk=id)
    form = Create_Post(instance=selcted_post)
    if request.method == 'POST':
        form = Create_Post(request.POST, instance=selcted_post)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home')

    return render(request, 'post/add-post.html', {'form': form})

@login_required
def DeletePost(request, id):
    selcted_post = Add_Post.objects.get(pk=id)
    selcted_post.delete()
    return redirect('home')

