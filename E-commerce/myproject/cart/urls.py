from django.urls import path
from cart.views import add_to_cart,cart,checkout ,hx_menu_cart
from cart import cart
from django.contrib.auth import views


urlpatterns = [
        path('hx_menu_cart/',hx_menu_cart,name='hx_menu_cart'),

    
    path('checkout/',checkout,name='checkout'),

    path('cart/',cart,name='cart'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    ]