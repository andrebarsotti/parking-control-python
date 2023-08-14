import uuid
from datetime import datetime

from django.db import models

class ParkingSpot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parking_spot_number = models.CharField(max_length=10, unique=True, null=False)
    license_plate_car = models.CharField(max_length=7, null=False)
    brand_car = models.CharField(max_length=70, null=False)
    model_car = models.CharField(max_length=70, null=False)
    color_car = models.CharField(max_length=70, null=False)
    registration_date = models.DateTimeField(null=False, default=datetime.now, editable=False)
    responsible = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    apartment = models.CharField(max_length=30, null=False)
    block = models.CharField(max_length=30, null=False)

    class Meta:
        ordering = ['registration_date']