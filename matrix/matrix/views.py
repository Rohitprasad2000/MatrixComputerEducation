from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
import smtplib
from email.message import EmailMessage


def index(request):
    return render(request, 'index.html')


def coaching(request):
    return render(request, 'coaching.html')


def time(request):
    return render(request, 'time.html')


def about(request):
    return render(request, 'about.html')


def enquiry(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message_contact = request.POST['message_contact']
        message_course = request.POST['message_course']
        E_name=message_name.capitalize()
        # messages_message = request.POST['message_message']

        # send mail
        send_mail(
            message_name,  # subject
            'I am '+ E_name+ ' and interested in ' + message_course + "\n "+'My contact Number is '+message_contact,  # message
            message_email,  # from mail
            ['prasadrohit098@gmail.com'],  # to mail
        )

        return render(request, 'Enquiry.html', {'message_name': message_name})

    else:
        return render(request, 'Enquiry.html')
