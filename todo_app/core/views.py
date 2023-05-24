from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.forms import JoinForm
from core.forms import LoginForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count, Case, When

from budget.models import Budget, BudgetCategory

from django.template.response import TemplateResponse
from .models import UserProfile
from django.contrib.auth.models import User


def create_userobj():
    for user in User.objects.all():
        UserProfile.objects.get_or_create(user=user)

def home(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'core_temp/index.html')

def join(request):
    if request.method == "POST":
        join_form = JoinForm(request.POST)
        profile_form = UserProfileForm()
        if join_form.is_valid():
            user = join_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("/")
        else:
            page_data = {"join_form": join_form, "profile_form": profile_form}
            return render(request, 'join.html', page_data)
    else:
        join_form = JoinForm()
        profile_form = UserProfileForm()
        page_data = {"join_form": join_form, "profile_form": profile_form}
        return render(request, 'join.html', page_data)

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect("/")
                else:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'login.html', {"login_form": LoginForm})
    else:
        return render(request, 'login.html', {"login_form": LoginForm})

def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")

