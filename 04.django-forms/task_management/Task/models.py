from django.db import models
from datetime import date
from Category.models import Category

# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=50, verbose_name='Task Title')
    taskDescription = models.TextField(verbose_name='Description')
    is_completed = models.BooleanField(default=False)
    TaskAssignDate = models.DateField(default=date.today, verbose_name='Assigning Date')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.taskTitle