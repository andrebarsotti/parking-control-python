from rest_framework import serializers
from parking_spot.models import ParkingSpot

class ParkingSpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = ['id', 'parking_spot_number', 'license_plate_car', 'brand_car', 'model_car', 'color_car', 'registration_date', 'responsible_name', 'apartment', 'block']
