from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from core.models import UserProfile
from .models import Task, TaskCategory
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Task

# Create your views here.

def index(request):
	return render(request, 'tasks_temp/task_list.html')




'''
class TaskList(ListView):
	model = Task
	template_name = "tasks_temp/task_list.html"
	context_object_name = 'tasks'
	
	
	def get_context_data(self, **kwargs):
		context = super(TaskList,self).get_context_data(**kwargs)
		context['form'] = checkform()
		#cur_user_state = UserProfile['tasks_view_hide_completed'].filter(user=self.request) # grab comp_task var
		if UserProfile.tasks_view_hide_completed is True: # if the user state true
			context['tasks'] = context['tasks'].filter(user=self.request.user,complete=False)
		else:
			context['tasks'] = context['tasks'].filter(user=self.request.user) # grab tasks from requested user
		return context
'''
class TaskList(ListView):
	model = Task
	template_name = "tasks_temp/task_list.html"
	context_object_name = 'tasks'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		#context['form'] = self.form
		#self.object = self.request.user
		#boolval = self.request.POST
		
		cur_user = User.objects.get(id=self.request.user.id)
		context['instance'] = UserProfile.objects.filter(user=self.request.user).get()
		profile = UserProfile.objects.filter(user=cur_user.id).get()
		#cur_user_state = UserProfile['tasks_view_hide_completed'].filter(user=self.request) # grab comp_task var
		if profile.tasks_view_hide_completed is True: # if the user state true
			context['tasks'] = context['tasks'].filter(user=self.request.user,complete=False)
		else:
			context['tasks'] = context['tasks'].filter(user=self.request.user) # grab tasks from requested user
		return context


	#form_class = checkform
'''
	def get(self, request, *args, **kwargs):
		self.object = self.request.user
		self.form = self.get_form(self.form_class)
		return ListView.get(self,request,*args, **kwargs)

	def post(self,request,*args,**kwargs):
		self.object = self.request.user
		self.form = self.get_form(self.form_class)

		if self.form.is_valid():
				self.object = self.form.save()
		return self.get(request, *args, **kwargs)
'''

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