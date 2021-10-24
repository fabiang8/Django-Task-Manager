from django.contrib import admin
from django.urls import	path,include
from . import views


urlpatterns = [
	
	path('budget', views.index, name="index2")

]
