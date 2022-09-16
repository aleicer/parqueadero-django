from rest_framework.serializers import ModelSerializer
from ticket.models import Ticket

class TicketSerializer(ModelSerializer):
  class Meta:
    model = Ticket
    fields = ['id', 'tarifa', 'hora_entrada','hora_salida','idVehiculo']