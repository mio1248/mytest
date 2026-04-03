from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'size', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'short_description')
    prepopulated_fields = {'slug': ('name',)}