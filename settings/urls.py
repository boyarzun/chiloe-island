from django.urls import path
from settings.views import index, template_options

app_name = 'settings'

urlpatterns = [
    path('settings', index, name='index'),
    path('settings/template', template_options, name='customizer'),
]

