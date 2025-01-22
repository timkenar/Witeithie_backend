from django.contrib import admin
from .models import Product, Cart, DeliveryAddress, Payment,Service,LandingPage

admin.site.register(LandingPage)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(DeliveryAddress)
admin.site.register(Payment)
admin.site.register(Service)
