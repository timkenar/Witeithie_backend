# rides/serializers.py
from rest_framework import serializers
from .models import Ride

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id', 'user', 'pickup_location', 'destination', 'driver_location', 'status', 'created_at', 'updated_at']
