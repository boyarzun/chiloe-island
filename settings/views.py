# Django
from django.shortcuts import render, get_object_or_404

# Models
from settings.models import Setting

# Forms
from settings.forms import SettingForm

def index(request):

    setting = get_object_or_404(Setting, pk=1)

    form = SettingForm(request.POST or None, instance=setting)
    context = {
        'menu': 'settings',
        'form': form
    }
    
    return render(request, 'settings/index.html', context)