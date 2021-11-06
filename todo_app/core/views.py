from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.forms import JoinForm
from core.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
#from.views import BudgetList,TaskList
from django.db.models import Count, Case, When
from tasks.models import Task
from budget.models import Budget, BudgetCategory
from tasks.models import Task, TaskCategory
from django.template.response import TemplateResponse
from .models import UserProfile
from django.contrib.auth.models import User
run_once = False

def populate_once(request):
    global run_once
    if run_once:
        return
    if BudgetCategory.objects.all():
        return    

    BudgetCategory.objects.create(category='Food')
    BudgetCategory.objects.create(category='Clothing')
    BudgetCategory.objects.create(category='Housing')
    BudgetCategory.objects.create(category='Education')
    BudgetCategory.objects.create(category='Entertainment')
    BudgetCategory.objects.create(category='other')

    TaskCategory.objects.create(category='Home')
    TaskCategory.objects.create(category='School')
    TaskCategory.objects.create(category='Work')
    TaskCategory.objects.create(category='Self Improvement')
    TaskCategory.objects.create(category='Other')

    run_once = True
def create_userobj():
    for user in User.objects.all():
        UserProfile.objects.get_or_create(user=user)

@login_required(login_url='/login/')
def home(request):
    populate_once(request)
    #create_userobj()
    actuallist =[]
    projectedlist=[]
    budget_list = Budget.objects.all().filter(user=request.user)
    for budget in budget_list:
        actuallist.append(budget.actual)
        projectedlist.append(budget.projected)

    num_comp = Task.objects.filter(user=request.user).aggregate(num_comp=Count(Case(When(complete=True,then=1))))
    num_fail = Task.objects.filter(user=request.user).aggregate(num_comp=Count(Case(When(complete=False,then=1))))
    num_list = []
    num_list.append(num_comp)
    num_list.append(num_fail)
    context = {
        "num_list": [num_comp,num_fail],
        "damn_lists": [actuallist,projectedlist]
    }
    return render(request, 'index.html', context)

# Create your views here.
def index(request):
    #populate_once(request)
    return render(request, 'core_temp/index.html')

def join(request):
	if (request.method == "POST"):
		join_form = JoinForm(request.POST)
		if (join_form.is_valid()):
			# Save form data to DB
			user = join_form.save()
			# Encrypt the password
			user.set_password(user.password)
			# Save encrypted password to DB
			user.save()
            
            # possibly create UserProfile object
			# Success! Redirect to home page.
			return redirect("/")
		else:
			# Form invalid, print errors to console
			page_data = { "join_form": join_form }
			return render(request, 'join.html', page_data)
	else:
		join_form = JoinForm()
		page_data = { "join_form": join_form }
		return render(request, 'join.html', page_data)

def user_login(request):
    #populate_once(request)
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                #Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request,user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'login.html', {"login_form": LoginForm})
    else:
        #Nothing has been provided for username or password.
        return render(request, 'login.html', {"login_form": LoginForm})

@login_required(login_url='/login/')
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")
