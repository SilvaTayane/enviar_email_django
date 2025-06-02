from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def envia_email(request):
    send_mail('Assunto', 'Esse é o email que estou te enviando', 
               'emanuelytayane22@gmail.com', 
               ['emanuelytayane604@gmail.com'],
               fail_silently=False,
               )
    return  HttpResponse('Olá')