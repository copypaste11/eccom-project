from products.models import Product, ProductCategory

from django.shortcuts import render

def index(request):
    context = {'title': 'Gaming Store'}
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
