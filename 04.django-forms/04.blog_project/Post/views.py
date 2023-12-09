from django.shortcuts import render, redirect
from .forms import Post_add_form

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