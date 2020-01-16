# Django
from django.shortcuts import render, redirect

# Models
from store.models import Product

def index(request):

        # Getting last products
        last_products = Product.objects.order_by('-id')[:6]

        context = {
                "last_products": last_products
        }

        #return render(request, "gijalan/index.html", context)
        return render(request, "coming-soon/index.html", context)