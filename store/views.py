# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Count
from django.urls import reverse

# Models
from store.models import Product, ProductCategory

# Forms
from store.forms import ProductForm

# Utils
from store.utils import index_filter

def index(request):


	context = index_filter(request)

	# Add categories to context
	categories = ProductCategory.objects.annotate(total_products=Count('productsubcategory__product'))
	context['categories'] = categories

	return render(request, "store/index.html", context)

@login_required
def products_index(request):

	products_list = Product.objects.all()

	page = request.GET.get('page', 1)
	
	# Pagination
	paginator = Paginator(list(products_list), 1)
	products = paginator.get_page(page)

	context = {
			'menu': 'products',
			'objects': products,
			'categories': ProductCategory.objects.all(),
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
			return redirect(reverse('store:products'))

	context = {
		'menu': 'products',
		'form': form,
		'categories': ProductCategory.objects.all(),
	}

	return render(request, 'products/create.html', context)