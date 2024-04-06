from django.views.generic import ListView, CreateView
from .models import Transaction
from django.urls import reverse_lazy

class TransactionListView(ListView):
    model = Transaction
    template_name = 'office_transactions/transaction_list.html'
    ordering = ['-date']



from .forms import TransactionForm

class TransactionCreateView(CreateView):
    model = Transaction
    template_name = 'office_transactions/transaction_form.html'
    form_class = TransactionForm
    success_url = reverse_lazy('transaction_list')
