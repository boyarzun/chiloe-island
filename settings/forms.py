# Django
from django import forms

# Models
from settings.models import Setting

class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ('name', 'slogan', 'logo', 'description', 'keywords')