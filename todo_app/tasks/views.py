from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Task, TaskCategory
from django.urls import reverse_lazy


from .models import Task

# Create your views here.

def index(request):
	return render(request, 'tasks_temp/task_list.html')


class TaskList(ListView):
	model = Task
	template_name = "tasks_temp/task_list.html"
	context_object_name = 'tasks'
	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tasks'] = context['tasks'].filter(user=self.request.user)
		return context

class TaskDetail(DetailView):
	model = Task
	context_object_name = 'task'
	template_name = "tasks_temp/task_detail.html"


class TaskCreate(CreateView):
	model = Task
	fields = ['description', 'category','complete']
	template_name = "tasks_temp/task_create.html"
	success_url = reverse_lazy('tasks')
	#success_url = ''

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(TaskCreate,self).form_valid(form)

class TaskCreateCategory(CreateView):
	model = TaskCategory
	fields = '__all__'
	template_name = "tasks_temp/task_category.html"
	success_url = reverse_lazy('tasks')
	#success_url = ''
	context_object_name = "category"


class DeleteCategory(DeleteView):
	model = TaskCategory
	context_object_name = "category"
	template_name = "tasks_temp/task_delete_category.html"
	success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
	model = Task
	fields = ['description', 'category', 'complete']
	template_name = "tasks_temp/task_create.html"
	success_url = reverse_lazy('tasks')

class DeleteView(DeleteView):
	model = Task
	context_object_name = "task"
	template_name = "tasks_temp/task_confirm_delete.html"
	success_url = reverse_lazy('tasks')