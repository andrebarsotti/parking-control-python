from django.contrib.auth.models import User
from rest_framework import serializers, validators
from parking_spot.models import ParkingSpot

class ParkingSpotSerializer(serializers.HyperlinkedModelSerializer):
    license_plate_car = serializers.CharField(max_length=7, required=True, allow_blank=False, validators=[validators.UniqueValidator(queryset=ParkingSpot.objects.all())])
    responsible = serializers.ReadOnlyField(source='responsible.username')

    class Meta:
        model = ParkingSpot
        fields = ['id', 'parking_spot_number', 'license_plate_car', 'brand_car', 'model_car', 'color_car', 'registration_date', 'responsible', 'apartment', 'block']
        validators = [
            validators.UniqueTogetherValidator(
                queryset=ParkingSpot.objects.all(),
                fields=['apartment', 'block']
            )
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')