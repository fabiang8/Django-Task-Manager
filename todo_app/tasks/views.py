from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from core.models import UserProfile
from .models import Task, TaskCategory
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from core.forms import checkform
from django.views.generic.edit import FormView

from .models import Task

# Create your views here.

def index(request):
	return render(request, 'tasks_temp/task_list.html')




'''
class TaskList(ListView, FormView):
	#model = Task
	queryset = Task.objects.all()
	template_name = "tasks_temp/task_list.html"
	context_object_name = 'tasks'
	form_class = checkform
	success_url = "tasks"
	def get_context_data(self, **kwargs):
		self.object_list = self.get_queryset()
		context = super(TaskList, self).get_context_data(**kwargs)
		#context['form'] = checkform()
		#userform = context['form'].filter(user=self.request.user).get()
		#if (userform.is_valid()):
		#	user = userform.save()
		#	user.save()
		#	return redirect("/")
		
		cur_user = User.objects.get(id=self.request.user.id)
		context['instance'] = UserProfile.objects.filter(user=self.request.user).get()
		profile = UserProfile.objects.filter(user=cur_user.id).get()
		#cur_user_state = UserProfile['tasks_view_hide_completed'].filter(user=self.request) # grab comp_task var
		if profile.tasks_view_hide_completed is True: # if the user state true
			context['tasks'] = context['tasks'].filter(user=self.request.user,complete=False)
		else:
			context['tasks'] = context['tasks'].filter(user=self.request.user) # grab tasks from requested user
		return context
	#def get_queryset(self):
		#data = self.model.objects.filter(user=self.request.user)

	def form_valid(self,form):
		instance1 = form.save(commit=False)
		instance1.user = self.request.user
		#UserProfile.objects.filter(user=self.request.user).get()
		instance1.save()
		return super(TaskList, self).form_valid(form)
		
'''
'''
class TaskList(ListView):
	model = Task
	template_name = "tasks_temp/task_list.html"
	context_object_name = 'tasks'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = checkform()
		#userform = context['form'].filter(user=self.request.user).get()
		#if (userform.is_valid()):
		#	user = userform.save()
		#	user.save()
		#	return redirect("/")

		#context['form'] = self.form
		#self.object = self.request.user
		#boolval = self.request.POST
		if self.request.method == 'POST':
			value = self.request.GET.get('checkbox')
		else:
			value = None
		cur_user = User.objects.get(id=self.request.user.id)
		profile = UserProfile.objects.filter(user=cur_user.id).get()
		#profile = UserProfile.objects.get(user=cur_user.id)
		#print(value)
		if value is None:
			#print("in on condition")
			#profile.set_hide
			#UserProfile.objects.filter(user=cur_user.id).get().set_hide()
			#cur_user.set_hide()
			print("bool value:",profile.tasks_view_hide_completed)
			print(profile)
		elif 'on' in value:
			#profile.tasks_view_hide_completed = False
			
			#UserProfile.objects.filter(user=cur_user.id).get().set_hide()
			profile.set_hide
			#cur_user.set_hide()
			print(profile)
			print("bool value:",profile.tasks_view_hide_completed)
		
		#context['instance'] = UserProfile.objects.filter(user=self.request.user).get()
		#cur_user_state = UserProfile['tasks_view_hide_completed'].filter(user=self.request) # grab comp_task var
		if profile.tasks_view_hide_completed is True: # if the user state true
		#if value is 'on':

			context['tasks'] = context['tasks'].filter(user=self.request.user,complete=False)
			print(self.request.user)
		elif profile.tasks_view_hide_completed is False:
			context['tasks'] = context['tasks'].filter(user=self.request.user) # grab tasks from requested user
			print(self.request.user)
		return context
'''

class TaskList(ListView):
	model = Task
	template_name = "tasks_temp/task_list.html"
	context_object_name = 'tasks'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = checkform()
		#userform = context['form'].filter(user=self.request.user).get()
		#if (userform.is_valid()):
		#	user = userform.save()
		#	user.save()
		#	return redirect("/")

		#context['form'] = self.form
		#self.object = self.request.user
		#boolval = self.request.POST
		
		#value = self.request.GET.get('checkbox')
		#context['value'] = value
		cur_user = User.objects.get(id=self.request.user.id)
		profile = UserProfile.objects.filter(user=cur_user.id).get()
		#profile = UserProfile.objects.get(user=cur_user.id)
		#print(value)
		'''
		if not value:
			#print("in on condition")
			profile.set_hide
			#UserProfile.objects.filter(user=cur_user.id).get().set_hide()
			#cur_user.set_hide()
			print("bool value:",profile.tasks_view_hide_completed)
			print(profile)
		elif value is None:
			#profile.tasks_view_hide_completed = False
			
			#UserProfile.objects.filter(user=cur_user.id).get().set_hide()
			#profile.set_hide
			#cur_user.set_hide()
			print(profile)
			print("bool value:",profile.tasks_view_hide_completed)
		'''
		#context['instance'] = UserProfile.objects.filter(user=self.request.user).get()
		#cur_user_state = UserProfile['tasks_view_hide_completed'].filter(user=self.request) # grab comp_task var
		print(profile.tasks_view_hide_completed)
		if profile.tasks_view_hide_completed is True: # if the user state true
		#if value is 'on':

			context['tasks'] = context['tasks'].filter(user=self.request.user,complete=False)
			print(self.request.user)
			return context
		elif profile.tasks_view_hide_completed is False:
			context['tasks'] = context['tasks'].filter(user=self.request.user) # grab tasks from requested user
			print(self.request.user)
			return context
		#return context










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

class UserUpdate(UpdateView):
	model = UserProfile
	form_class = checkform
	template_name = "tasks_temp/update_user.html"
	success_url = reverse_lazy('tasks')
	pk_url_kwarg = 'UserProfile_pk'
	context_object_name = 'UserProfile'

	'''
	def get_context_data(self, *args, **kwargs):
		context = super(UserUpdate, self).get_context_data(*args,**kwargs)
		return context
	'''
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