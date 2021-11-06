from django.contrib import admin
from django.urls import	path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, TaskCreateCategory, DeleteCategory



urlpatterns = [
	#path('', TaskList.as_view()),
	path('tasks', TaskList.as_view(), name='tasks'),
	#path('tasks/set_hide/', set_hide, name='hide'),
	path('tasks/task_detail/<int:pk>/', TaskDetail.as_view(), name='task'),
	path('tasks/create_task/', TaskCreate.as_view(), name='task-create'),
	#path('tasks/create_task_category/', TaskCreateCategory.as_view(), name='task-category'),
	path('tasks/task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
	path('tasks/task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
	#path('tasks/category-delete/', DeleteCategory.as_view(), name='category-delete'),

]
