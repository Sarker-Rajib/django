from django.shortcuts import render

# Create your views here.



def about(request):
    # print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        return render(request, 'first_app/about.html', {'name':name, 'email': email})
    else:
       return render(request, 'first_app/about.html')

def index(request):
    return render(request, 'first_app/index.html')
        