from django.urls import path
from contact.views import *

app_name = 'contact'

urlpatterns = [
    # Public store
    path('contact', index, name="index"),
]

