from django import forms
from authentication.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        labels = {
            'username': 'Nombre usuario',
            'email': 'Correo',
            'password': 'Contraseña',
            'address': 'Dirección',
            'phone': 'Telefono',
        }

        widgets = {'address':forms.TextInput(attrs={'placeholder':'Direccion'}),
                    'phone':forms.NumberInput(attrs={'placeholder':'Telefono'}),
                    }

        exclude = ('user','birthdate','gender')

