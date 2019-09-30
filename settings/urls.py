from django.urls import path
from settings.views import index

app_name = 'settings'

urlpatterns = [
    path('', index, name='index'),
]

