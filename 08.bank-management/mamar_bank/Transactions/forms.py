from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Transactions

class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['account', 'amount']

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super.__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()

    def save(self, commit = True):
        self.instance.account = self.account
        self.instance.balance_amount = self.account.balance
        return super().save()
    
class DepositForm(Transactions):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit minumum amount : {min_deposit_amount}'
            )
        return amount

class WithdrawForm(Transactions):
    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance
        amount = self.cleaned_data.get('amount')
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You need to withdraw minumum amount : {min_withdraw_amount}'
            )

        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw max amount : {max_withdraw_amount}'
            )

        if balance < amount:
            raise forms.ValidationError(
                f'You dont have enough money !'
            )
        
        return amount
    
class LoanRequestForm(Transactions):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        return amount
