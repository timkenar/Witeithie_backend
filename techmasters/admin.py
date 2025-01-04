from django.contrib import admin
from .models import Product, Cart, DeliveryAddress, Payment

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(DeliveryAddress)
admin.site.register(Payment)
