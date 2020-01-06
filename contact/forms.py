# Django
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=100)
    subject = forms.CharField(max_length=128)
    message = forms.CharField(max_length=500)
