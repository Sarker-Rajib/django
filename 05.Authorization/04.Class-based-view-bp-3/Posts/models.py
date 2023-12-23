from django.db import models
from Category.models import Add_Category
from django.contrib.auth.models import User

# Create your models here.
class Add_Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    category = models.ManyToManyField(Add_Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/media/images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Add_Post, on_delete=models.CASCADE, related_name ='comments')
    name = models.CharField(max_length = 30)
    email = models.EmailField(unique=True)
    body = models.TextField()
    creates_on= models.DateField(auto_now_add = True)

    def __str__(self):
        return f'Comments by {self.name}'

