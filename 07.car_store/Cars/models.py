from django.db import models
from Brands.models import Brand

# Create your models here.
class Car(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length = 45)
    description = models.TextField()
    quantity = models.TextField()
    price = models.CharField(max_length = 45)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)



# There will be two models: Car Model and Brand Model. 
# Make a relationship between them so that A brand has multiple cars but a car must have only one brand. 
# You can add additional apps/models if you need.
# In the car details page there will be a 
# car image, name, description, quantity, price, brand name a