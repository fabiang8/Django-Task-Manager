from django.contrib import admin
from django.urls import	path,include
from . import views


urlpatterns = [
	
	path('task_page', views.index, name="index3")

]
