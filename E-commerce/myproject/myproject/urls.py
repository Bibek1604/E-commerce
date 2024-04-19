
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from myapp.views import frontpage, shop

from myapp.views import frontpage, shop
from product.views import product_view  # Corrected import
from product.models import Product, Category  # Capitalized Product and Category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('product/', product_view, name='product'),
]