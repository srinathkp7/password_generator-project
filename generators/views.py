from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generators/home.html')


def password(request):

    character = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRST'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        character.extend(list('1234567890'))
    length = int(request.GET.get('length',10))


    thepassword = ''

    for x in range(length):
        thepassword += random.choice(character)

    return render(request, 'generators/password.html', {"password":thepassword})
