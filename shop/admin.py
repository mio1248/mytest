from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'size',
        'is_active',
        'is_featured',
        'featured_order',
    )
    list_display_links = ('id', 'name')
    list_editable = ('is_active', 'is_featured', 'featured_order')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'short_description', 'description')
    list_filter = ('is_active', 'is_featured', 'created_at')
    ordering = ('featured_order', 'id')
    fieldsets = (
        (
            '기본 정보',
            {
                'fields': (
                    'name',
                    'slug',
                    'image',
                    'price',
                    'size',
                    'short_description',
                    'description',
                )
            },
        ),
        (
            '노출 설정',
            {
                'fields': ('is_active', 'is_featured', 'featured_order'),
                'description': '대표 상품으로 체크한 상품만 메인 화면에 최대 6개까지 노출됩니다.',
            },
        ),
    )
