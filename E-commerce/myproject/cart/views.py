from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .cart import Cart
from .models import Product


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/menu_cart.html')


def cart(request):
    cart=Cart(request, 'cart.html')
    
    print(cart)
    for item in cart:
        print(item)
    return render(request, 'cart.html')

def update_cart(request, product_id, action):
    cart = Cart(request)
    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)
    
    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)['quantity']
    
    item = {
        'product': {
            'id': product.id,
            'name': product.name,
            'image': product.image,
            'get_thumbnail': product.get_thumbnail(),  # Changed from 'get.thumbnail' to 'thumbnail'
            'price': product.price,
        },
        'total_price': (quantity * product.price) / 100,  # Assuming price is in cents
        'quantity': quantity,
    }
    response = render(request, 'partial/cart_item.html', {"item": item})
    response['HX-Trigger'] = 'update-menu-cart'  # Changed 'Hx_trigger' to 'HX-Trigger'
    
    return response

@login_required
def cart(request):
    return render (request,'cart/')


def get_item(self , product_id):
    return self.cart[str(product_id)]