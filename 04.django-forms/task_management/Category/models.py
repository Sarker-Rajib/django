from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=50, verbose_name='Category title')

    def __str__(self):
        return self.categoryName