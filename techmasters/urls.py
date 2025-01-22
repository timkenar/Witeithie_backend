from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartViewSet, DeliveryAddressViewSet, PaymentViewSet,LandingPageViewSet

router = DefaultRouter()
router.register(r'landing-page', LandingPageViewSet, basename="landing-page")
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet)
router.register(r'delivery-address', DeliveryAddressViewSet)
router.register(r'payment', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
