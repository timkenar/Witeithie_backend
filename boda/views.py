# rides/views.py
from rest_framework import viewsets
from .models import Ride
from .serializers import RideSerializer
from rest_framework.permissions import IsAuthenticated

class RideViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing ride instances.
    """
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Assign the logged-in user as the ride creator
        serializer.save(user=self.request.user)
