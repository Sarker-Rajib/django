from django.db import models
from Brands.models import Brand

# Create your models here.
class Car(models.Model):
    image = models.ImageField(upload_to='cars/media/images/')
    name = models.CharField(max_length = 45)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name