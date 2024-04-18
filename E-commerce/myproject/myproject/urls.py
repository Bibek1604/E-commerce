
from django.contrib import admin
from django.urls import path

from myapp.views import frontpage,shop
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',frontpage,name='frontpage'),
    path('shop/',shop,name='shop'),

]
