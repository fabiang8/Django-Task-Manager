from django.contrib import admin
from django.urls import	path,include
from . import views


urlpatterns = [
	
	path('', views.home, name="home"),
	path('admin/', admin.site.urls),
	path('core_home_page/',views.index,name="index1"),
	path('join/',views.join, name="join"),
	path('login/',views.user_login, name="login"),
	path('logout/',views.user_logout, name="logout"),
]

