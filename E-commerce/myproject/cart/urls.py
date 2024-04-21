from django.urls import path
from cart.views import add_to_cart,cart,checkout 
from cart import cart
from django.contrib.auth import views


urlpatterns = [

    path('cart/',cart,name='cart'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    ]