from django.shortcuts import get_object_or_404, render

from .models import Product


def index(request):
    featured_products = Product.objects.filter(
        is_active=True,
        is_featured=True,
    ).order_by('featured_order', 'id')[:6]
    return render(request, 'index.html', {'featured_products': featured_products})


def shop_list(request):
    products = Product.objects.filter(is_active=True).order_by('featured_order', 'id')
    return render(request, 'shop_list.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'product_detail.html', {'product': product})
