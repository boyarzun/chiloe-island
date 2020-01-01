# Django
from django import forms

# Models
from store.models import Product

class ProductForm(forms.ModelForm):

    images_status = forms.CharField(max_length=20, widget=forms.HiddenInput(), initial='0::0::0')

    class Meta:
        model = Product
        exclude = ('pk',)

    def is_valid(self):
        """Return True if the form has no errors, or False otherwise."""
        splittedValue = self.data['images_status'].split('::')

        if (splittedValue[0] == '1'):
            self.initial.image_one.delete()
        elif (splittedValue[1] == '1'):
            self.initial.image_two.delete()
        elif (splittedValue[2] == '1'):
            self.initial.image_three.delete()

        return self.is_bound and not self.errors