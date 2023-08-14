from django.urls import path, include
from rest_framework import routers
from parking_spot import views

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'parking-spot', views.ParkingSpotViewSet, basename='parking-spot')
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
