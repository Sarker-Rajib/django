from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def formOne(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'formTemplates/formOne.html', {'form': StudentForm})
    else:
        form = StudentForm()
        return render(request, 'formTemplates/formOne.html', {'form': StudentForm})