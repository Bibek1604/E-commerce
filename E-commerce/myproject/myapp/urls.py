from django.urls import path
from myapp.views import frontpage, shop, signup, login_old

from product.views import product
from django.contrib.auth import views



urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_old, name='login'),
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('login/',views.LoginView.as_view(template_name='login.html'),name='login'),
    path('shop/<slug:slug>/', product, name='product'),

]
