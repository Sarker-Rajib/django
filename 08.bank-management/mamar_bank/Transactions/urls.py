from django.urls import path
from .views import DepositMoneyView, WithdrawMoneyView, TransactionsReportView,LoanRequestView,LoanListView,PayLoanView, TransferMoney


# app_name = 'transactions'
urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
    path("transfer/", TransferMoney.as_view(), name="transfer"),
    path("loan_request/", LoanRequestView.as_view(), name="loan_request"),
    path("report/", TransactionsReportView.as_view(), name="transaction_report"),
    path("loans/", LoanListView.as_view(), name="loan_list"),
    path("loans/<int:loan_id>/", PayLoanView.as_view(), name="pay"),
]