from django.shortcuts import get_object_or_404, render

from .models import Product


def index(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'index.html', {'products': products})



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'product_detail.html', {'product': product})
