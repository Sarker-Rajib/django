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
    

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=20, verbose_name='Your Name')
    body = models.TextField(verbose_name='Your Comment')
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Feedback by {self.name}"