from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from core.models import UserProfile
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']

        # send email

        send_mail(
            'Inquiry from :' + message_name , # subject
            message,# Email message
            message_email,# from
            ['arrive.transport06906@gmail.com'], # to 
            )

        return render(request, 'tasks_temp/task_list.html', {'message_name' : message_name})
    else:
        return render(request, 'tasks_temp/task_list.html')



