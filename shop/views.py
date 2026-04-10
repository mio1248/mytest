from django.db import OperationalError, ProgrammingError
from django.shortcuts import get_object_or_404, render

from .models import Product



def _get_main_products():
    base_qs = Product.objects.filter(is_active=True)
    try:
        featured = list(base_qs.filter(is_featured=True).order_by('featured_order', 'id')[:6])
        if featured:
            return featured
    except (OperationalError, ProgrammingError):
        pass
    return list(base_qs.order_by('id')[:6])



def index(request):
    products = _get_main_products()
    return render(request, 'index.html', {'products': products})



def shop_list(request):
    try:
        products = list(Product.objects.filter(is_active=True).order_by('featured_order', 'id'))
    except (OperationalError, ProgrammingError):
        products = list(Product.objects.filter(is_active=True).order_by('id'))
    return render(request, 'shop_list.html', {'products': products})



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'product_detail.html', {'product': product})
