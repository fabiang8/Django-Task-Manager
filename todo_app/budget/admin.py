from django.contrib import admin
from .models import Budget, BudgetCategory

# Register your models here.
admin.site.register(BudgetCategory)
admin.site.register(Budget)