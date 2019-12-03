from django.urls import path
from store.views import *

app_name = 'store'

urlpatterns = [
    path('store', index, name="index"),
    path('products/', products_index, name="products"),
    path('products/new', products_create, name="new"),
]

