from rest_framework import viewsets
from .models import Product, Cart, DeliveryAddress, Payment, LandingPage
from .serializers import ProductSerializer, CartSerializer, DeliveryAddressSerializer, PaymentSerializer, LandingPageSerializer
# techmasters/views.py

from rest_framework.viewsets import ModelViewSet

class LandingPageViewSet(ModelViewSet):
    """
    API endpoint to manage landing page content.
    """
    queryset = LandingPage.objects.all()
    serializer_class = LandingPageSerializer

    def get_queryset(self):
        # Ensure only one LandingPage is returned, modify logic as needed.
        return super().get_queryset().order_by("-updated_at")

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DeliveryAddressViewSet(viewsets.ModelViewSet):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
