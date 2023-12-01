from django.shortcuts import render
# nav app
# Create your views here.
def nav_home(request):
    return render(request, "navIndev.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact-us.html")