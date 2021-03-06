# Django
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from authentication.forms import UserProfileForm, UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.urls import reverse, reverse_lazy

# Models
from django.contrib.auth.models import User
from settings.models import Setting

# CCBV
from django.contrib.auth.views import PasswordResetView

def login(request):
    # We check if the user is loggin
    if request.user.is_authenticated:
        return redirect(reverse_lazy('store:mystore'))
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
                return redirect(reverse_lazy('store:mystore'))

    # Si llegamos al final renderizamos el formulario
    return render(
        request,
        "authentication/login.html",
        {'form': form}
        )

def register(request):
    template = 'authentication/register.html'
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            #messages.success(request, "Usuario registrado")
            return HttpResponseRedirect(reverse('log:login'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    data = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, template, data)

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

class AuthenticationPasswordResetView(PasswordResetView):
            
    html_email_template_name = 'registration/password_reset_email_html.html'
    success_url = reverse_lazy('authentication:password_reset_done')

    def __init__(self, **kwargs):
        """
        Constructor. Called in the URLconf; can contain helpful extra
        keyword arguments, and other things.
        """
        # Go through keyword arguments, and either save their values to our
        # instance, or raise an error.

        for key, value in kwargs.items():
            setattr(self, key, value)

        setattr(self, 'extra_email_context', self.set_extra_email_context())


    def set_extra_email_context(self):
        settings = Setting.objects.get(pk=1)
        context = {
            'SITE_NAME': settings.name,
            'SITE_PHONE_NUMBER': settings.phone_number,
            'SOCIAL_NETWORKS': {
                'INSTAGRAM': settings.instagram,
                'FACEBOOK': settings.facebook,
                'TWITTER': settings.twitter,
            }
        }
        return context