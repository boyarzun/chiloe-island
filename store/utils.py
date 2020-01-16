# Django
from django.core.paginator import Paginator

# Models
from store.models import Product
from django.db.models import Max, Min


def index_filter(request, seller=None):
    
    sort = int(request.GET.get('sort', 0))
    price_min = request.GET.get('min')
    price_max = request.GET.get('max')
    categories = request.GET.get('categories')

    products_list = Product.objects.filter(active=True).order_by('-created_at')

    if seller:
        products_list = products_list.filter(seller=seller)

    range_max = products_list.aggregate(Max('price'))['price__max']
    range_min = products_list.aggregate(Min('price'))['price__min']

    if price_min and price_max:
        products_list = products_list.filter(price__gte=price_min, price__lte=price_max)

    if categories:
        categories = categories.split('::')
        products_list = products_list.filter(categories__category__in=categories)


    if sort == 1:
        products_list = products_list.order_by('name')
    elif sort == 2:
        products_list = products_list.order_by('-name')
    elif sort == 3:
        products_list = products_list.order_by('-price')
    elif sort == 4:
        products_list = products_list.order_by('price')

    """ Pagination """
    # epp = elements per page
    epp = 16
    page = request.GET.get('page')
    paginator = Paginator(list(products_list), epp)
    products = paginator.get_page(page)


    """ Context """

    context = {
        "products": products,
        "filter": {
            "range": {
                "max": range_max,
                "min": range_min,
            },
            "sort": {
                "selected": sort
            }
        }
    }

    return context

def get_last_products(seller, quantity, current_product):

    last_products = Product.objects.filter(seller=seller)
    
    if current_product:
        last_products = last_products.exclude(id = current_product.id)
        
    last_products = last_products.order_by('-pk')[0:quantity]

    return last_products
