# main_folder
from django.shortcuts import render
import datetime

def home(request):
    date = datetime.datetime.now()
    comment = "08:00 1 June 2006"
    persons = [
        {
            'name': "Rajib",
            'age':30
        },
        {
            'name': "Tannee",
            'age': 22
        },
        {
            'name': "Bohnee",
            'age': 9
        },
        {
            'name': "Aohnee",
            'age': 9
        },
    ]
    tagA = "<h2 >We will see filters</h2>"
    data = {'arr' : [1,2,3,4,5,6], "date" : date ,"arr2": ['2','1','3','4','5'], "string": "hello there its me" , 'number': 56, 'bool':False, 'persons': persons, 'sym': tagA, 'comment':comment}
    return render(request, 'index.html', data)