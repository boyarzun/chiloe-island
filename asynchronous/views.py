import string
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

def create_user_random(cantidad):
    for x in range(cantidad):
        username = 'usuario_{}'.format(get_random_string(5, string.ascii_letters))
        email = '{}@miempresa.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} Usuarios creados correctamente'.format(x)