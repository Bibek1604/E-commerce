from django.urls import path
from myapp.views import frontpage, shop  # Corrected import

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),  # Assuming 'shop' is your view function for the shop page
]
