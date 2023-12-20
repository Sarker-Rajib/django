from django.shortcuts import render
from Posts.models import Add_Post
from Category.models import Add_Category

# Create your views here.
def index(request, category_slug = None):
    cats = Add_Category.objects.all()
    posts = Add_Post.objects.all()
    
    if category_slug is not None:
        category = Add_Category.objects.get(slug = category_slug)
        posts = Add_Post.objects.filter(category = category)
        
    return render(request, 'index.html', {'posts': posts, 'categories': cats})