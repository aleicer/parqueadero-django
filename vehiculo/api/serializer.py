from rest_framework.serializers import ModelSerializer
from vehiculo.models import Vehiculo

class VehiculoSerializer(ModelSerializer):
  class Meta:
    model = Vehiculo
    fields = ['id', 'placa', 'tipo_vehiculo']