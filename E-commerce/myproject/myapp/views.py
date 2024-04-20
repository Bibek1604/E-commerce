from django.shortcuts import render
from django.db.models import Q
from product.models import Category, Product  # Corrected import

def get_categories():
    return Category.objects.all()

def frontpage(request):
    products =Product.objects.all()[0:8]
    # context = {'categories': categories}
    return render(request, 'frontpage.html', {'products':products})

def shop(request, slug=None):  # Updated function signature
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
    
    return render(request, 'shop.html', context)

def product_view(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product': product}
    return render(request, 'product.html', context)
