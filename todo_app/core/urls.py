from django.contrib import admin
from django.urls import	path,include
from . import views


urlpatterns = [
	
	path('', views.home, name="home"),
	path('core_home_page',views.index,name="index1"),
]
