from django.urls import path
from product.views import get_products, do_search


urlpatterns = [
    path('', get_products, name='products'),
    path('search/', do_search, name='search'),
   
]