from django.shortcuts import render
from Posts.models import Add_Post

# Create your views here.
def index(request):
    data = Add_Post.objects.all()
    return render(request, 'index.html', {'data': data})