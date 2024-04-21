from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from cart.views import add_to_cart
from product.views import product
from cart import cart

urlpatterns = [
    path('',include('myapp.urls')),
    path('',include('cart.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# incase use path    path('cart/checkout',cart,name='checkout'),
