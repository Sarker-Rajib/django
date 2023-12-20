from django.shortcuts import render, redirect
from .forms import Create_Post
from .models import Add_Post
from django.contrib import messages

# Create your views here.
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

def EditPost(request, id):
    selcted_post = Add_Post.objects.get(pk=id)
    postForm = Create_Post(instance=selcted_post)
    if request.method == 'POST':
        postForm = Create_Post(request.POST, instance=selcted_post)
        if postForm.is_valid():
            postForm.save()
            return redirect('home')

    return render(request, 'post/add-post.html', {'form': postForm})

def DeletePost(request, id):
    selcted_post = Add_Post.objects.get(pk=id)
    selcted_post.delete()
    return redirect('home')