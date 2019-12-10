from django.urls import path
from store.views import *

app_name = 'store'

urlpatterns = [
    path('store', index, name="index"),
    path('mystore/', mystore_index, name="mystore"),
    path('mystore/new', products_create, name="new"),
]

