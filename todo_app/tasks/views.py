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
        message_name = request.POST['name']
        message_email = request.POST['email']
        phone = request.POST['phone']
        pickup = request.POST['pickup']
        destination = request.POST['destination']
        message = request.POST['message']


        # send email

        send_mail(
            'Inquiry from :' + message_name , # subject
            'Message: ' + message +'.\n' + 'Inquiry Email: ' + message_email  + '.\n' + '(Phone: ' + phone + ', Pickup: '  + pickup +  ', Destinaton: ' + destination + '.)\n' ,
            message_email,
            ['arrive.transport06906@gmail.com'], # to 
            )

        return render(request, 'tasks_temp/task_list.html', {'message_name' : message_name})
    else:
        return render(request, 'tasks_temp/task_list.html')



