# Django
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Models
from settings.models import Setting

# Forms
from settings.forms import SettingForm

def index(request):

    setting = get_object_or_404(Setting, pk=1)

    if request.method == 'POST':
        form = SettingForm(data=request.POST, files=request.FILES, instance=setting)
        form.save()
        messages.success(request, "Sitio actualizado!")
    else:
        form = SettingForm(instance=setting)

    context = {
        'menu': 'settings',
        'form': form
    }
    
    return render(request, 'settings/index.html', context)