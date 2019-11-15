# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse

# Models
from store.models import Product

# Forms
from store.forms import ProductForm

@login_required
def index(request):
        return render(request, "store/index.html", context)

@login_required
def products_index(request):

        products_list = Product.objects.all()

        # Pagination
        paginator = Paginator(list(products_list), 15)
        products = paginator.get_page(1)

        context = {
                'menu': 'products',
                'objects': products
        }

        return render(request, 'products/index.html', context)

@login_required
def products_create(request):

		form = ProductForm()

		if request.method == 'POST':
			request.POST = request.POST.copy()
			request.POST['user'] = str(request.user.id)
			form = ProductForm(data=request.POST, files=request.FILES)
			if form.is_valid():
				form.save()
				messages.success(request, "Producto agregado!")
				return redirect(reverse('store:products'))

		context = {
			'menu': 'products',
			'form': form,
		}

		return render(request, 'products/create.html', context)