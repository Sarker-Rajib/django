from django.shortcuts import render
from .form import contactform

# Create your views here.

def about(request):
    # print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        number = request.POST.get('number')
        return render(request, 'first_app/about.html', {'name':name, 'email': email, 'number':number})
    else:
       return render(request, 'first_app/about.html')

def index(request):
    return render(request, 'first_app/index.html')

def djangoform(request):
    form = contactform(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'first_app/djangoform.html', {'form':form})