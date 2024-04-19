from django.shortcuts import render

def product_view(request):
    return render(request, 'product/product.html')
