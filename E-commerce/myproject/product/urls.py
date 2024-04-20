from django.urls import path
from myapp.views import frontpage, shop, shop_view

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', shop_view, name='shop_detail'),
]
