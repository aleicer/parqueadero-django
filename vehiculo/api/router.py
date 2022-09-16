from rest_framework.routers import DefaultRouter
from vehiculo.api.views import VehiculoApiViewSet

router_vehiculo = DefaultRouter()

router_vehiculo.register(prefix = 'vehiculo', basename = 'vehiculo', viewset = VehiculoApiViewSet)