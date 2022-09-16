from django.contrib import admin

from ticket.models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
  list_display = ['id','tarifa','hora_entrada','hora_salida']