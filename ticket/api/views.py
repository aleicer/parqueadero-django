from rest_framework.viewsets import ModelViewSet
from ticket.models import Ticket  
from ticket.api.serializer import TicketSerializer

class TicketApiViewSet(ModelViewSet):
  serializer_class = TicketSerializer
  queryset = Ticket.objects.all()