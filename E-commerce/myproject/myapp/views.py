from django.shortcuts import render
from product.models import product,Category
from django.db.models import Q

# Create your views here.
def frontpage(request):
    
    products=product.objects.all()[0:8]
    return render (request, 'frontpage.html',{'products':products})

def shop(request):
    Categories = Category.objects.all()
    products=product.objects.all()
    
    active_category =request.GET.get('category','')
    if active_category:
        products=products.filter(Category_slug=active_category)
        
        query=request.Get.get('query',' ')
        
        if query:
            products=products.filter(Q(name_icontains = query))
    
    context={
        'categories':Categories,
        'products':products,
        'active_category':active_category,
    }
    
    
    
    return render(request, 'shop.html',{'products':products})
 