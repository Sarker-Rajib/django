from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView , ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transactions
from .constant import Deposit, Withdraw, Loan, Loan_Paid
from .forms import DepositForm, WithdrawForm, LoanRequestForm
from django.contrib import messages
from datetime import datetime

# Create your views here.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = ''
    model = Transactions
    title = ''
    success_url = ''

    def get_form_kwargs(self):
        kwargs=  super().get_form_kwargs()
        kwargs.update({
            'account' : self.request.user.account 
        })
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title' : self.title
        })

class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'

    def get_initial(self):
        initial = {'transaction_type': Deposit}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields = ['balance']
        )

        messages.success(self.request, f'Amount {amount} Deposit Succeessful.')
        return super().form_valid(form)

class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdwaw Money'

    def get_initial(self):
        initial = {'transaction_type': Withdraw}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance -= amount
        account.save(
            update_fields = ['balance']
        )

        messages.success(self.request, f'Amount {amount} Withdraw Succeessful.')
        return super().form_valid(form)
    
class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Loan Request'

    def get_initial(self):
        initial = {'transaction_type': Loan}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        current_loan_count = Transactions.objects.filter(account = account, transaction_type=3, loan_approve=True).count()

        if current_loan_count >= 3:
            return HttpResponse('You have crossed the limits')

        messages.success(self.request, f'Loan request sent to Admin')
        return super().form_valid(form)

class TransactionsReportView(LoginRequiredMixin, ListView):
    template_name =''
    model = Transactions
    balance = 0

    def get_queryset(self):
        querySet = super().get_queryset().filter(
            account = self.request.user.account
        )

        start_date_s = self.response_class.GET.get('start_date')
        end_date_s = self.response_class.GET.get('end_date')

        if start_date and end_date:
            start_date = datetime.strptime(start_date_s, "%Y-%M-%Y").date()
            end_date = datetime.strptime(end_date_s, "%Y-%M-%Y").date()

            # querySet = querySet.filter(
            #     timestamp_date_gte = start_date, 
            #     timestamp_date_lte = end_date
            # )

            self.balance = Transactions.objects.filter(
                 timestamp_date_gte = start_date, 
                 timestamp_date_lte = end_date
            ).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance
        
        return querySet.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account' : self.request.user.account
        })

        return context