from django.db import models

# Create your models here.
class Add_Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=110, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name