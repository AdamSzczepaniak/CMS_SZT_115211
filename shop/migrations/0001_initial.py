# Generated by Django 2.1.3 on 2019-01-05 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('create_date', models.DateTimeField(verbose_name='Create date')),
                ('write_date', models.DateTimeField(verbose_name='Last write date')),
                ('first_name', models.CharField(max_length=20, verbose_name='First name')),
                ('last_name', models.CharField(max_length=25, verbose_name='Last name')),
                ('street', models.CharField(max_length=40, verbose_name='Street')),
                ('zip_code', models.CharField(max_length=10, verbose_name='Zip code')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('email', models.CharField(max_length=35, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(verbose_name='Create date')),
                ('write_date', models.DateTimeField(verbose_name='Last write date')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Total cost')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(verbose_name='Create date')),
                ('write_date', models.DateTimeField(verbose_name='Last write date')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='shop.Order')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(verbose_name='Create date')),
                ('write_date', models.DateTimeField(verbose_name='Last write date')),
                ('parent_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop.ProductCategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('create_date', models.DateTimeField(verbose_name='Create date')),
                ('write_date', models.DateTimeField(verbose_name='Last write date')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('create_date', models.DateTimeField(verbose_name='Create date')),
                ('write_date', models.DateTimeField(verbose_name='Last write date')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price')),
                ('external_code', models.CharField(max_length=15)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ProductCategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(verbose_name='Create date')),
                ('write_date', models.DateTimeField(verbose_name='Last write date')),
                ('ean', models.CharField(max_length=20, verbose_name='Barcode')),
                ('external_code', models.CharField(max_length=30, verbose_name='External code')),
                ('product_tmpl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variants', to='shop.ProductTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='VariantName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('create_date', models.DateTimeField(verbose_name='Create date')),
                ('write_date', models.DateTimeField(verbose_name='Last write date')),
            ],
        ),
        migrations.CreateModel(
            name='VariantType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('create_date', models.DateTimeField(verbose_name='Create date')),
                ('write_date', models.DateTimeField(verbose_name='Last write date')),
            ],
        ),
        migrations.AddField(
            model_name='variantname',
            name='variant_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variant_names', to='shop.VariantType'),
        ),
        migrations.AddField(
            model_name='producttemplate',
            name='variants',
            field=models.ManyToManyField(to='shop.VariantName'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product_tmpl_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tmpl_images', to='shop.ProductTemplate'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product_var_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='var_images', to='shop.ProductVariant'),
        ),
        migrations.AddField(
            model_name='client',
            name='shopcart_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='shop.Order'),
        ),
        migrations.AddField(
            model_name='client',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL),
        ),
    ]