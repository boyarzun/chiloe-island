from django.urls import path
from store.views import *

app_name = 'store'

urlpatterns = [
    # Public store
    path('store', index, name="index"),
    path('store/<int:id_product>', seller_product, name="sellerproduct"),
    path('@<slug:store_name>', seller_store, name="sellerstore"),
    # Dashboard
    path('mystore/', mystore_index, name="mystore"),
    path('mystore/new', products_create, name="new"),
    path('mystore/<int:product_id>', product_edit, name="edit"),
]

