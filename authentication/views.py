from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from authentication.forms import UserProfileForm, UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse

def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        print(request)
        return render(request, "authentication/welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(
        request,
        "authentication/login.html",
        {'form': form}
        )

def register(request):
    template = 'authentication/register.html'
   


    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/')

    context = {
        'form': form
    }

    return render(request, template, context)

def reset(request):

    return render(
        request,
        "authentication/forgot-password.html",
        )

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
