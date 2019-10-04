from django.urls import path
from settings.views import index

app_name = 'settings'

urlpatterns = [
    path('settings', index, name='index'),
]

