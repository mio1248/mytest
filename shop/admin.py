from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_active', 'is_featured', 'featured_order', 'created_at')
    list_display_links = ('id', 'name')
    list_editable = ('is_active', 'is_featured', 'featured_order')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'short_description', 'description')
    list_filter = ('is_active', 'is_featured', 'created_at')
    ordering = ('featured_order', 'id')
