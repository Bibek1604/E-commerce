from django.contrib import admin
from django.urls import path
from myapp.views import frontpage, shop, product_view

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product_view, name='product'),  # Assuming 'product_view' is your view function for the product page
    path('admin/', admin.site.urls),
]
