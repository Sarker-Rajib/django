from django.shortcuts import render, redirect
from .forms import Post_add_form
from .models import Post

# Create your views here.
def AddPost(request):
    if request.method == 'POST':
        postForm = Post_add_form(request.POST)
        if postForm.is_valid():
            postForm.save()
            return redirect('add-post')
    else:
        postForm = Post_add_form() 
        return render(request, 'post/add-post.html', {'form': postForm})

def EditPost(request, id):
    selcted_post = Post.objects.get(pk=id)
    postForm = Post_add_form(instance=selcted_post)
    if request.method == 'POST':
        postForm = Post_add_form(request.POST, instance=selcted_post)
        if postForm.is_valid():
            postForm.save()
            return redirect('home')

    return render(request, 'post/add-post.html', {'form': postForm})

def DeletePost(request, id):
    selcted_post = Post.objects.get(pk=id)
    selcted_post.delete()
    return redirect('home')
