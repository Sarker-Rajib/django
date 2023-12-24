from django.db import models
from Cars.models import Car
from django.contrib.auth.models import User

# Create your models here.
class MyCars(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.car.name