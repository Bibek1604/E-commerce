from django.contrib import admin
from django.urls import path
from myapp.views import frontpage, shop  # Updated import statement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('shop/<slug>/', shop, name='shop'),
  # Updated path to use 'shop' instead of 'shop_view'
]
