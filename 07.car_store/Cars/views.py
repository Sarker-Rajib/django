from django.shortcuts import render
from .forms import AddCar
from .models import Car
from django.views.generic import DetailView

# Create your views here.
def add_car(request):
    form = AddCar
    return render(request, 'car/add-car.html', {'form': form})

class CarDetails(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'car/car-details.html'
    context_object_name = 'car'

    # def post(self, request, *args, **kwargs):
    #     comment_form = Create_Comment(data=self.request.POST)
    #     post = self.get_object()
    #     if comment_form.is_valid():
    #         new_comment = comment_form.save()
    #         new_comment.post = post
    #         new_comment.save()
    #     return self.get(request, *args, **kwargs)