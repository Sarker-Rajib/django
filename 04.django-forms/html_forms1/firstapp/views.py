from django.shortcuts import render
from .form import contactform, studentData, PasswordValidation

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
    if request.method == 'POST':
        form = contactform(request.POST, request.FILES)

        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./firstapp/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, 'first_app/djangoform.html', {'form':form})
    
    else:
        form = contactform()
        return render(request, 'first_app/djangoform.html', {'form':form})


def studentForm(request):
    if request.method == 'POST':
        form = studentData(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'first_app/validat-form.html', {'form':form})
    
    else:
        form = studentData()
        return render(request, 'first_app/validat-form.html', {'form':form})


def passwordmatch(request):
    if request.method == 'POST':
        form = PasswordValidation(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data)

        return render(request, 'first_app/password-match.html', {'form':form})
    
    else:
        form = PasswordValidation()
        return render(request, 'first_app/password-match.html', {'form':form})
