from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return HttpResponse("Core core.py")
# Create your views here.
