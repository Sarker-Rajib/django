from django.db import models
from datetime import date

# Create your models here.
class Musician(models.Model):
    FirstName = models.CharField(max_length=40, verbose_name='First Name', default='Mr. ')
    LastName = models.CharField(max_length=40, verbose_name='Last Name')
    Email = models.EmailField(verbose_name='Enter Your email')
    PhoneNumber = models.CharField(max_length=11, verbose_name='Phone Number')
    InstrumentType = models.CharField(max_length=20, verbose_name='Instrument Type')

    def __str__(self):
        return self.FirstName

class Album(models.Model):
    AlbumName = models.CharField(max_length=40, verbose_name='Album Name')
    Artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    CHOISES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]
    rating = models.CharField(choices=CHOISES ,max_length=5, default=None)
    ReleaseDate = models.DateField(default=date.today)