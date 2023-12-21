from django.db import models
from Category.models import Add_Category
from django.contrib.auth.models import User

# Create your models here.
class Add_Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    category = models.ManyToManyField(Add_Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title