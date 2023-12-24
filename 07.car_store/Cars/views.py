from django.shortcuts import render
from .forms import AddCar, CommentForm
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

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = self.object.comments.all()
        comment_form = CommentForm()

        context['comments'] = comments        
        context['comment_form'] = comment_form
        return context