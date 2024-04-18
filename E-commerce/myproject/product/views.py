from django.shortcuts import render
from product.models import Product, Category


# Create your views here.
def product_view(request):
    return render(request, 'product/product.html')
