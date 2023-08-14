from rest_framework import viewsets
from parking_spot.models import ParkingSpot
from parking_spot.serializers import ParkingSpotSerializer

class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer