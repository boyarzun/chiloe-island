# Django
from django import forms

# Models
from authentication.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nombre de tienda'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address', 'phone')
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Dirección'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Teléfono'}),
        }

