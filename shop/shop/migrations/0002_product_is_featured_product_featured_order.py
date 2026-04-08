from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured_order',
            field=models.PositiveIntegerField(default=0, verbose_name='대표 상품 순서'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='대표 상품 여부'),
        ),
    ]
