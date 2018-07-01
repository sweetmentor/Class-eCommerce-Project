from django.urls import path
from product.views import get_products


urlpatterns = [
    path('', get_products, name='products'),
    # path('search_products/', search_products, name='match'),
    
]