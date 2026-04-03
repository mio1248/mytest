from django.db import models


from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField('상품명', max_length=100)
    slug = models.SlugField('슬러그', unique=True, allow_unicode=True)
    image = models.ImageField('상품이미지', upload_to='products/')
    short_description = models.CharField('짧은 설명', max_length=200)
    description = models.TextField('상세 설명')
    price = models.PositiveIntegerField('가격')
    size = models.CharField('규격', max_length=100, blank=True)
    is_active = models.BooleanField('진열 여부', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = '상품'
        verbose_name_plural = '상품'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])