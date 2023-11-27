from django.shortcuts import render

# navbar app folder
# Create your views here.
def about(request):
    return render(request, 'navbar/about.html')

def contact(request):
    return render(request, 'navbar/contact.html')
