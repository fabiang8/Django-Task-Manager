from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return HttpResponse("Budget Budget.py")
# Create your views here.
