from django.urls import path
from events.views import *

app_name = 'events'

urlpatterns = [
    # Public
    path('events', index, name="index"),
]

