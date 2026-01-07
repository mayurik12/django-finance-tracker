from django.shortcuts import render, redirect, HttpResponse 
from django.views import View
from Finance.forms import RegisterForm, TransactionForm, GoalForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction, Goal
from django.db.models import Sum
from.admin import TransactionResource 
from django.contrib import messages

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
           user = form.save()
           login(request, user)
           messages.success(request, "Account created successfully!")
           return redirect('dashboard')
        #         return redirect('/admin/')   # change if needed
        return render(request, "register.html", {'form': form})

class DashboardView(LoginRequiredMixin, View):
    def get(self,request):
        transactions = Transaction.objects.filter(user = request.user)
        goal = Goal.objects.filter(user = request.user)

        # Calculate total income and expenses
        total_income = Transaction.objects.filter(user = request.user,
        transaction_type__iexact='income').aggregate(Sum('amount'))['amount__sum'] or 0

        total_expense = Transaction.objects.filter(user = request.user,
        transaction_type__iexact='expense').aggregate(Sum('amount'))['amount__sum'] or 0

        net_saving = total_income - total_expense

        remaining_savings = net_saving

        goal_progress = []

        for g in goal:
            if remaining_savings >= g.target:
                goal_progress.append({'goal':g, 'progress':100})
                remaining_savings -= g.target

            elif remaining_savings > 0:
                progress = (remaining_savings / g.target) * 100
                goal_progress.append({'goal':g, 'progress':progress})
                
                remaining_savings = 0
               
            else:
                goal_progress.append({'goal':g, 'progress':0})

        
        context = {

            'transactions' : transactions,
            'total_income' : total_income,
            'total_expense' : total_expense,
            'net_saving' : net_saving,
            'goal_progress': goal_progress,
        }
        return render(request,"dashboard.html", context)
    
class TransactionCreateView(LoginRequiredMixin,View):
    def get(self,request):
        form = TransactionForm()
        return render(request,"transaction_form.html", {'form': form})
    
    def post(self, request):
        form = TransactionForm(request.POST)
        if form.is_valid():
           transaction = form.save(commit=False)
           transaction.user = request.user
           transaction.save()
           messages.success(request, 'Transaction added successfully!')
           return redirect('dashboard')
        return render(request, "transaction_form.html", {'form': form})
        
class TransactionListView(LoginRequiredMixin, View):
    def get(self, request):
        transactions = Transaction.objects.filter(user = request.user)
        return render(request, "transaction_list.html", {'transactions': transactions})

class GoalCreateView(LoginRequiredMixin,View):
    def get(self,request):
        form = GoalForm()
        return render(request,"goal_form.html", {'form': form})
    
    def post(self, request):
        form = GoalForm(request.POST)
        if form.is_valid():
           goal = form.save(commit=False)
           goal.user = request.user
           goal.save()
           messages.success(request, 'Goal added successfully!')
           return redirect('dashboard')
        return render(request, "goal_form.html", {'form': form})

def export_transaction(request):
    user_transactions = Transaction.objects.filter(user = request.user)

    transactions_resource = TransactionResource()
    dataset = transactions_resource.export(queryset = user_transactions)

    excel_data = dataset.export('xlsx')

    response = HttpResponse(excel_data, content_type = 'application/' \
    'vnd.opemxmlformats-officedocument.spreadsheetml.sheet')

    response['content-Disposition'] = 'attachment; filename = transaction_report.xlsx'
    return response  
