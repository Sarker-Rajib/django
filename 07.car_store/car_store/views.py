from django.shortcuts import render
from Cars.models import Car
from Brands.models import Brand

# Create your views here.
def home(request, brand_slug = None):
    cars = Car.objects.all()
    brands = Brand.objects.all()

    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        cars = Car.objects.filter(brand_name = brand)
    return render(request, 'index.html', {'data':cars, 'brand':brands})