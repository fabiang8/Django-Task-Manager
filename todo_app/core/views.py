from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.forms import JoinForm
from core.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
#from.views import BudgetList,TaskList
from django.db.models import Count, Case, When
from tasks.models import Task
from django.template.response import TemplateResponse

@login_required(login_url='/login/')
def home(request):

    num_comp = Task.objects.filter(user=request.user).aggregate(num_comp=Count(Case(When(complete=True,then=1))))
    num_fail = Task.objects.filter(user=request.user).aggregate(num_comp=Count(Case(When(complete=False,then=1))))
    num_list = []
    num_list.append(num_comp)
    num_list.append(num_fail)
    context = {
        "num_list": [num_comp,num_fail]
    }
    return render(request, 'index.html', context)

# Create your views here.
def index(request):
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
