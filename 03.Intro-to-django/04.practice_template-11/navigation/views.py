from django.shortcuts import render
# nav app
# Create your views here.
def nav_home(request):
    return render(request, "navIndev.html")

def about(request, id):
    return render(request, "about.html", {'id':id})

def contact(request):
    print(request.GET)
    return render(request, "contact-us.html")