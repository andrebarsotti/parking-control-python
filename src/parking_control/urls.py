from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from parking_spot import views

router = routers.DefaultRouter()
router.register(r'parking_spot', views.ParkingSpotViewSet, basename='parking-spot')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
