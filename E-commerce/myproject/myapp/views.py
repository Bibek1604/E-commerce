from django.shortcuts import render
from product.models import product


# Create your views here.
def frontpage(request):
    products=product.objects.all()[0:8]
    return render (request, 'frontpage.html',{'products':products})

def shop(request):
    products=product.objects.all()
    return render(request, 'shop.html',{'products':products})
 