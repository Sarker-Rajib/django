from typing import Any
from django.contrib import admin
from .models import Transactions

# Register your models here.
@admin.register(Transactions)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'balance_amount', 'transaction_type', 'loan_approve']
    def save_model(self, request, obj, form, change):

        if obj.loan_approve == True:
            obj.account.balance += obj.amount
            obj.balance_amount = obj.account.balance
            obj.account.save()
        super().save_model(request, obj, form, change)