# Django
from django import forms

# Models
from store.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('pk',)