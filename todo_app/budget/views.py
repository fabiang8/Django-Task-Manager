from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, 'budget_temp/budget.html')
# Create your views here.
