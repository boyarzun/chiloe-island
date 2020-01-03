# Django
from django import forms

# Models
from store.models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('pk',)

    def is_valid(self):
        """Return True if the form has no errors, or False otherwise."""

        if self.files and self.initial:
            for key in self.files:
                try:
                    self.initial[key].delete()
                except ValueError:
                    pass

        return self.is_bound and not self.errors