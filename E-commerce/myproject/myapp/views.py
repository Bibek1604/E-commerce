from django.shortcuts import render
from product.models import product, Category  # Capitalize Product and Category
from django.db.models import Q
from django.shortcuts import render

def frontpage(request):
    return render(request, 'frontpage.html')

def shop(request):
    categories = Category.objects.all()  # Use lowercase for variable names
    products = product.objects.all()
    
    active_category = request.GET.get('category', '')
    if active_category:
        products = products.filter(category__slug=active_category)  # Use double underscore for foreign key fields
        
    query = request.GET.get('query', '')  # Fix the typo from Get to GET
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category,
    }
    
    return render(request, 'shop.html', context)
