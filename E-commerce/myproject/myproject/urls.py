from django.contrib import admin
from django.urls import path
from myapp.views import frontpage, shop
from product.views import product_view
from product.models import Product, Category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('shop/<slug:slug>/', shop, name='shop'),  # Removed extra space
    path('product/', product_view, name='product'),
]
