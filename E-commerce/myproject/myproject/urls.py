from django.urls import path
from myapp.views import frontpage, shop  
from django.contrib import admin# Corrected import
from product.views import product
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),  
    path('product/', product, name='product'),  
]
