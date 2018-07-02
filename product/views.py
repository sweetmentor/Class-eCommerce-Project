from django.shortcuts import render, get_object_or_404 
from .models import Product

# Create your views here ----- products.
def get_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products': products})
    
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['query'])
    return render(request, "products/products.html", {"products": products})