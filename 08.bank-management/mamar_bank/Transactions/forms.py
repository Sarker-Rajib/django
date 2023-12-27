from django import forms
from django.forms.utils import ErrorList
from .models import Transactions

class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['amount', 'transaction_type']

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()

    def save(self, commit = True):
        self.instance.account = self.account
        self.instance.balance_amount = self.account.balance
        return super().save()
    
class DepositForm(TransactionsForm):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit minumum amount : {min_deposit_amount}'
            )
        return amount

class WithdrawForm(TransactionsForm):
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
    
class LoanRequestForm(TransactionsForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        return amount
