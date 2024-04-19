from django.shortcuts import render
from .models import Product

def product_view(request, slug):
    product =Product.objects.get(slug=slug)
    return render(request, 'product/product.html')
