from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, redirect
from django.views.generic import CreateView , ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transactions
from .constant import Deposit, Withdraw, Loan, Loan_Paid
from .forms import DepositForm, WithdrawForm, LoanRequestForm
from django.contrib import messages
from datetime import datetime
from django.db.models import Sum
from django.views import View
from django.urls import reverse_lazy

# Create your views here.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transactions/transaction_form.html'
    model = Transactions
    title = ''
    success_url = reverse_lazy('transaction_report')

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

        return context

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
    title = 'Withdraw Money'

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
    template_name ='transactions/transaction_report.html'
    model = Transactions
    balance = 0

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.account
        )
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')
        
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            
            queryset = queryset.filter(timestamp__date__gte=start_date, timestamp__date__lte=end_date)
            self.balance = Transactions.objects.filter(
                timestamp__date__gte=start_date, timestamp__date__lte=end_date
            ).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance
       
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })

        return context


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account' : self.request.user.account
        })

        return context

class PayLoanView(LoginRequiredMixin, View):
    def get(self, request, loan_id):
        loan = get_object_or_404(Transactions, id=loan_id)
        print(loan)
        if loan.loan_approve:
            user_account = loan.account

            if loan.amount < user_account.balance:
                user_account.balance -= loan.amount
                loan.balance_amount = user_account.balance
                user_account.save()
                loan.loan_approve = True
                loan.transaction_type = Loan_Paid
                loan.save()
                return redirect('loan_list')
            else:
                messages.error( self.request, f'Loan amount is greater than available balance')

        return redirect('loan_list')

class LoanListView(LoginRequiredMixin,ListView):
    model = Transactions
    template_name = 'transactions/loan_request.html'
    context_object_name = 'loans' 
    
    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transactions.objects.filter(account=user_account,transaction_type=3)
        print(queryset)
        return queryset

