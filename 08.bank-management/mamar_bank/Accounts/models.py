from django.db import models
from django.contrib.auth.models import User
from .constants import acc_type, gender_type

# Create your models here.
class UserBankAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    Acctp = models.CharField(max_length=10, choices=acc_type, verbose_name='Account Type')
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_type)
    initial_deposit_date=models.DateField(auto_now_add=True)
    balance=models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.account_no}'


class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    street_address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    postal_code=models.IntegerField()

    def __str__(self) -> str:
        return f'{self.user.account.account_no}'