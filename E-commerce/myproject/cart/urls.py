from django.urls import path
from cart.views import add_to_cart,cart,checkout ,hx_menu_cart,update_cart,hx_cart_total
from cart import cart
from django.contrib.auth import views


urlpatterns = [
        path('hx_menu_cart/',hx_menu_cart,name='hx_menu_cart'),

    
    path('checkout/',checkout,name='checkout'),
    path('update_cart/<int:product_id>/<str:action>',update_cart,name='update_cart'),
    path('hx_cart_total/',hx_cart_total,name='hx_cart_total'),


    path('cart/',cart,name='cart'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    ]