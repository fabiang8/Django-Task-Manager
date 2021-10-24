
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, 'index.html')
# Create your views here.
def index(request):
	return render(request, 'core_temp/index.html')
