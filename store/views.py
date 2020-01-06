# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Count
from django.urls import reverse

# Models
from store.models import Product, Category
from django.contrib.auth.models import User

# Forms
from store.forms import ProductForm

# Utils
from store.utils import index_filter, get_last_products
from core.utils import prepare_number_phone_to_whatsapp

def index(request):

	context = index_filter(request)

	# Add categories to context
	categories = Category.objects.annotate(total_products=Count('subcategory__product'))
	context['categories'] = categories
	context['pagination'] = {
		'total': context['products'].paginator.count,
		'from': context['products'].start_index,
		'to': context['products'].end_index,
		}

	return render(request, "store/index.html", context)

@login_required
def mystore_index(request):

	products_list = Product.objects.filter(seller=request.user)

	page = request.GET.get('page', 1)
	
	# Pagination
	paginator = Paginator(list(products_list), 9)
	products = paginator.get_page(page)

	context = {
			'menu': 'products',
			'objects': products,
			'categories': Category.objects.all(),
	}

	return render(request, 'products/index.html', context)

@login_required
def products_create(request):

	form = ProductForm()

	if request.method == 'POST':
		request.POST = request.POST.copy()
		request.POST['seller'] = str(request.user.id)
		form = ProductForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, "Producto agregado!")
			return redirect(reverse('store:mystore'))

	context = {
		'menu': 'products',
		'form': form,
		'categories': Category.objects.all(),
	}

	return render(request, 'products/create.html', context)

@login_required
def product_edit(request, product_id):

	product = get_object_or_404(Product, pk=product_id)

	form = ProductForm(instance=product)

	if request.method == 'POST':
		request.POST = request.POST.copy()
		request.POST['seller'] = str(request.user.id)
		form = ProductForm(data=request.POST, files=request.FILES, instance=product)
		if form.is_valid():
			form.save()
			messages.success(request, "Producto actualizado!")
			return redirect(reverse('store:mystore'))

	context = {
		'menu': 'products',
		'form': form,
		'categories': Category.objects.all(),
	}

	return render(request, 'products/edit.html', context)


def seller_store(request, store_name):

	store = get_object_or_404(User, username=store_name)

	context = index_filter(request, store)

	# Add categories to context
	categories = Category.objects.annotate(total_products=Count('subcategory__product'))
	context['categories'] = categories
	context['store'] = store
	context['pagination'] = {
		'total': context['products'].paginator.count,
		'from': context['products'].start_index,
		'to': context['products'].end_index,
		}

	return render(request, "store/seller_store.html", context)

def seller_product(request, id_product):

	product = get_object_or_404(Product, pk=id_product)

	whatsapp = prepare_number_phone_to_whatsapp(product.seller.userprofile.phone)

	context = {
		"product": product,
		"last_products": get_last_products(product.seller, 2),
		"whatsapp": { "phone": whatsapp }
	}

	return render(request, "store/seller_product.html" , context)