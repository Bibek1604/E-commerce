from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib.auth import login

from product.models import Product, Category
from cart.views import login_required

from .forms import SignUpForm
def frontpage(request):
    products = Product.objects.all()[0:8]

    return render(request, 'frontpage.html', {'products': products})

def signup(request):
    if request.method == 'POST':
        form =SignUpForm(request.POST)
        
        if form.is_valid():
            user =form.save()
            login(request,user)
            return redirect('/')
        else:
            form=SignUpForm() 
            
    return render(request, 'signup.html', {'form':form})

def login_old(request):
    return render(request, 'login.html')

@login_required
def edit_myaccount(request):
    return render(request, 'edit_myaccount.html')

@login_required
def myaccount(request):
    if request.method == "POST":
  
        
        user=request.user
        user.first_name = request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        
        return redirect('myaccount')
        
    return render(request, 'myaccount.html')
    


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }

    return render(request, 'shop.html', context)

def hx_menu_cart(request):
    return render(request,'menu_cart.html')