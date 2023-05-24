from django.contrib import admin
from django.urls import	path,include
from .views import BudgetList, BudgetCreate, BudgetUpdate, BudgetDelete


urlpatterns = [
	
	path('budgets', BudgetList.as_view(), name="budgets"),
	path('budgets/create_budget/', BudgetCreate.as_view(), name="create-budget"),
	path('budgets/update_budget/<int:pk>/', BudgetUpdate.as_view(), name="update-budget"),
	path('budgets/delete_budget/<int:pk>/', BudgetDelete.as_view(), name="delete-budget"),
]
