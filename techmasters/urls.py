from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartViewSet, DeliveryAddressViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet)
router.register(r'delivery-address', DeliveryAddressViewSet)
router.register(r'payment', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
