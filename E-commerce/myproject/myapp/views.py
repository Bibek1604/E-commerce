from django.shortcuts import render
from product.models import Product, Category  # Corrected Product and Category capitalization
from django.db.models import Q

def frontpage(request):
    return render(request, 'frontpage.html')

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()  # Corrected Product capitalization
    
    active_category = request.GET.get('category', '')
    if active_category:
        products = products.filter(category__slug=active_category)
        
    query = request.GET.get('query', '')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category,
    }
    
    return render(request, 'shop.html', context)
