from django.shortcuts import render
import datetime

# navbar app folder
# Create your views here.
def about(request):
    return render(request, 'navbar/about.html')

def contact(request):
    d = {'author' : 'Rajib', 'age':21, 'arrs' : ['I', 'am', 'Rajib'], 'birtday': datetime.datetime.now(),'list':[{
            "name":"Rajib",
            "age": 29
        },
        {
            "name":"Sarker",
            "age": 28
        },]}
    return render(request, 'navbar/contact.html',d)
