from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop_list, name='shop_list'),
    path('product/<str:slug>/', views.product_detail, name='product_detail'),
]
