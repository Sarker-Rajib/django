from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import Create_Post
from .models import Add_Post
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# class based view
from django.views.generic import CreateView, UpdateView, DeleteView

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

# class views
@method_decorator(login_required, name='dispatch')
class AddPostByClass(CreateView):
    model = Add_Post
    form_class = Create_Post
    template_name = 'post/add-post.html'
    success_url = reverse_lazy('add-post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditPostByClass(UpdateView):
    model = Add_Post
    form_class = Create_Post
    template_name = 'post/add-post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

@method_decorator(login_required, name='dispatch')
class DeletePostByClass(DeleteView):
    model = Add_Post
    template_name = 'post/delete-post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
