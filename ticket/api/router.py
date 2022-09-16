from rest_framework.routers import DefaultRouter
from ticket.api.views import TicketApiViewSet

router_ticket = DefaultRouter()

router_ticket.register(prefix = 'ticket', basename = 'ticket', viewset = TicketApiViewSet)