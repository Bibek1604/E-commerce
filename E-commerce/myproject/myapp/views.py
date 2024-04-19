from django.shortcuts import render
from django.db.models import Q
from product.models import Category, Product
from django.http import HttpResponse


def get_categories():
    return Category.objects.all()

def frontpage(request):
    categories = get_categories()
    context = {'categories': categories}
    return HttpResponse(request, 'frontpage.html', context)

def shop(request):
    categories = get_categories()
    products = Product.objects.all()
    
    active_category_slug = request.GET.get('category', '')
    if active_category_slug:
        products = products.filter(category__slug=active_category_slug)
        
    query = request.GET.get('query', '')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    context = {
        'categories': categories,
        'products': products,
        'active_category_slug': active_category_slug,
    }
    
    return HttpResponse(request, 'shop.html', context)
