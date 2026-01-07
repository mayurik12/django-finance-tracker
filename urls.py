from django.urls import path
from .views import RegisterView, DashboardView,TransactionCreateView, TransactionListView,GoalCreateView,export_transaction


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', DashboardView.as_view(), name='dashboard'),
    path('add/', TransactionCreateView.as_view(), name = 'transaction_add'),
    path('transaction/', TransactionListView.as_view(), name='transaction_list'),
    path('goal/', GoalCreateView.as_view(), name = "goal_add"),
    path('generate-report/', export_transaction, name = 'export_transaction'),
]
