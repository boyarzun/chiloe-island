# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages

# Models
from settings.models import Setting

# Forms
from settings.forms import SettingForm

@login_required
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

@login_required
def template_options(request):

    setting = Setting.objects.get(pk=1)

    param = list(request.GET.keys())[0]
    value = request.GET.get(param)
    value = int(value) if value.isdigit else value
    value = bool(value) if type(getattr(setting, param)) == bool else value

    setattr(setting, param, value)

    setting.save()

    return JsonResponse({
        param: getattr(setting, param)
    })