from django.db import models

######################## --- PRODUCTS --- ################################

class ProductCategory(models.Model):
    name = models.CharField(max_length=60)
    create_date = models.DateTimeField('Create date')
    write_date = models.DateTimeField('Last write date')
    parent_id = models.ForeignKey('self', blank=True, null=False, related_name='children')

class ProductImage(models.Model):
    name = models.CharField(max_length=120)
    create_date = models.DateTimeField('Create date')
    write_date = models.DateTimeField('Last write date')
    image = models.ImageField()
    product_tmpl_id = models.ForeignKey('ProductTemplate', related_name='tmpl_images')
    product_var_id = models.ForeignKey('ProductVariant', related_name='var_images')

class ProductTemplate(models.Model):
    name = models.CharField(max_length=120)
    create_date = models.DateTimeField('Create date')
    write_date = models.DateTimeField('Last write date')
    price = models.DecimalField('Price', null=False, blank=False, max_digits=8, decimal_places=2)
    category_id = models.ForeignKey('ProductCategory')
    external_code = models.CharField(max_length=15)
    variants = models.ManyToManyField('VariantName')

class ProductVariant(models.Model):
    name =  models.CharField(max_length=200)
    create_date = models.DateTimeField('Create date')
    write_date = models.DateTimeField('Last write date')
    ean = models.CharField('Barcode', max_length=20)
    external_code = models.CharField('External code', max_length=30)
    product_tmpl_id = models.ForeignKey('ProductTemplate', related_name='product_variants')

class VariantType(models.Model):
    name = models.CharField(max_length=120)
    create_date = models.DateTimeField('Create date')
    write_date = models.DateTimeField('Last write date')

class VariantName(models.Model):
    name = models.CharField(max_length=120)
    create_date = models.DateTimeField('Create date')
    write_date = models.DateTimeField('Last write date')
    variant_type_id = models.ForeignKey('VariantType', related_name='variant_names')

############################# --- ORDERS --- #############################################

class Order(models.Model):
    name = models.CharField(max_lenght=60)
    create_date = models.DateTimeField('Create date')
    write_date = models.DateTimeField('Last write date')
    total_cost = models.DecimalField('Total cost', max_digits=9, decimal_places=2)

class OrderProduct(models.Model):
    create_date = models.DateTimeField('Create date')
    write_date = models.DateTimeField('Last write date')
    quantity = models.IntegerField('Quantity')
    order_id = models.ForeignKey('Order', related_name='order_products')

############################# --- CLIENTS --- ############################################

class Client(models.Model):
    name = models.CharField(max_length=120)
    create_date = models.DateTimeField('Create date')
    write_date = models.DateTimeField('Last write date')
    first_name = models.CharField('First name', max_length=20)
    last_name = models.CharField('Last name', max_length=25)
    street = models.CharField('Street', max_length=40)
    zip_code = models.CharField('Zip code', max_length=10)
    city = models.CharField('City', max_length=30)
    email = models.CharField('Email', max_lenght=35)
    shopcart_id = models.ForeignKey('Order', related_name='client')
    user_id = models.ForeignKey('User', related_name='client')


