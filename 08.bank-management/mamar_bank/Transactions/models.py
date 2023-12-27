from django.db import models
from Accounts.models import UserBankAccount
from .constant import t_type

# Create your models here.
class Transactions(models.Model):
    account = models.ForeignKey(UserBankAccount, on_delete=models.CASCADE, related_name='transaction')
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    balance_amount = models.DecimalField(decimal_places=2, max_digits=12)
    transaction_type = models.IntegerField(choices=t_type)
    timestamp= models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']