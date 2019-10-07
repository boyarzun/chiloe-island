# Django
from django import forms

# Models
from authentication.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields=('username', 'email','password')
    
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # check for min length
        min_length = 8
        if len(password) < min_length:
            msg = 'Password must be at least %s characters long.' %(str(min_length))
            self.add_error('password', msg)

        # check for digit
        if sum(c.isdigit() for c in password) < 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('password', msg)

        # check for uppercase letter
        if not any(c.isupper() for c in password):
            msg = 'Password must contain at least 1 uppercase letter.'
            self.add_error('password', msg)

        # check for lowercase letter
        if not any(c.islower() for c in password):
            msg = 'Password must contain at least 1 lowercase letter.'
            self.add_error('password', msg)
            
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

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

