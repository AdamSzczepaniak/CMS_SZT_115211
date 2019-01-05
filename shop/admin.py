from django.contrib import admin

from .models import ProductCategory, ProductTemplate, ProductVariant, VariantType, VariantName, Order, OrderProduct, Client

admin.site.register(ProductCategory)
admin.site.register(ProductTemplate)
admin.site.register(ProductVariant)
admin.site.register(VariantType)
admin.site.register(VariantName)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Client)