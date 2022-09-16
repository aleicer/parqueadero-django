from rest_framework.viewsets import ModelViewSet
from vehiculo.models import Vehiculo  
from vehiculo.api.serializer import VehiculoSerializer

class VehiculoApiViewSet(ModelViewSet):
  serializer_class = VehiculoSerializer
  queryset = Vehiculo.objects.all()