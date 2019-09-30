from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from authentication.forms import UserProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
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
    if request.POST:
        form = UserProfileForm(request.POST)

        if form.is_valid() and not User.objects.filter(username=request.POST['username']).exists():
            user = User.objects.create_user(username=request.POST['username'],
                                            email=request.POST['email'],
                                            password=request.POST['password'])
            form = form.save(commit=False)
            form.user = user
            form.save()
            #messages.success(request, "Usuario registrado")
            return HttpResponseRedirect(reverse('log:login'))
    else:
        form = UserProfileForm()

    # Si llegamos al final renderizamos el formulario
    return render(
        request,
        "authentication/register.html",
        {'form': form}
        )

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
