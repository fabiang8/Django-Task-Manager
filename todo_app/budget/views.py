from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Budget, BudgetCategory
from django.urls import reverse_lazy
from django.db.models import Sum, F, IntegerField
from django.db.models.functions import Coalesce


def index(request):
	return render(request, 'budget_temp/index.html')
# Create your views here.

class BudgetList(ListView):
	model = Budget
	template_name = "budget_temp/budget_list.html"
	context_object_name	= 'budgets'


#	queryset = Budget.objects.annotate(
#	projectsum_= Coalesce(Sum('actual'), Value(0)) - Coalesce(Sum('projected'), Value(0))
#	)    	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		qs = kwargs.pop('object_list', self.object_list)
		actual = qs.filter(user=self.request.user).aggregate(actual=Sum('actual'))
		projected = qs.filter(user=self.request.user).aggregate(projected=Sum('projected'))
		if projected['projected']:
			actual = float(projected['projected']) - float(actual['actual'])
		#balance = int(balance)
		context['budgets'] = context['budgets'].filter(user=self.request.user)
		context['actual'] = actual
		return context
	
#	def get_total(self):
#		actual_val = Budget.objects.all().aggregate(
#			budget_left = Sum(F('actual') - F('projected'), output_field=IntegerField())
#			)
#		return actual_val



class BudgetDetail(DetailView):
	model = Budget
	context_object_name = 'budget'
	template_name = "budget_temp/budget_detail.html"




class BudgetCreate(CreateView):
	model = Budget
	fields = ['description','category','projected','actual']
	template_name = "budget_temp/budget_create.html"
	success_url = reverse_lazy('budgets')

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(BudgetCreate,self).form_valid(form)

class BudgetUpdate(UpdateView):
	model = Budget
	fields = ['description','category','projected','actual']
	template_name = "budget_temp/budget_create.html"
	success_url = reverse_lazy('budgets')

class BudgetDelete(DeleteView):
	model = Budget
	context_object_name ="budget"
	template_name = "budget_temp/budget_delete.html"
	success_url = reverse_lazy('budgets')

