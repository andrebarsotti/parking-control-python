from django.contrib.auth.models import User
from rest_framework import serializers
from parking_spot.models import ParkingSpot

class ParkingSpotSerializer(serializers.HyperlinkedModelSerializer):
    responsible = serializers.ReadOnlyField(source='responsible.username')

    class Meta:
        model = ParkingSpot
        fields = ['id', 'parking_spot_number', 'license_plate_car', 'brand_car', 'model_car', 'color_car', 'registration_date', 'responsible', 'apartment', 'block']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')