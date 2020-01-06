# Django
from django import forms

# Models
from store.models import Product

class ProductForm(forms.ModelForm):

    images_status = forms.CharField(max_length=20, widget=forms.HiddenInput(), initial='0::0::0::0')

    class Meta:
        model = Product
        exclude = ('pk',)

    def is_valid(self):
        """Return True if the form has no errors, or False otherwise."""

        if self.initial:
            splittedValue = self.data['images_status'].split('::')

            if (splittedValue[1] == '1'):
                self.initial['image_two'].delete()
            if (splittedValue[2] == '1'):
                self.initial['image_three'].delete()
            if (splittedValue[3] == '1'):
                self.initial['image_four'].delete()

        if self.files and self.initial:
            for key in self.files:
                try:
                    self.initial[key].delete()
                except ValueError:
                    pass

        return self.is_bound and not self.errors